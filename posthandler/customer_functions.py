from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta;
import traceback
import json


def review(data):
    status={}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uid=u.values('uid')
        v=Users.objects.filter(Vendor__shop_name=data.POST['Shop_name'])
        vid=u.values('vid')
        review=data.POST['Review']
        ratings=data.POST['Rating']
        rev=ReviewsRating(cid=uid,vid=vid,review=review,rating=ratings)
        rev.save()
        status['stat']="success"
    except:
        status['stat']="fail"

    return status


def set_payment(data):
    status={}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        cid=u.values('uid')
        payment_Dets=data.POST["payment_dets"]
        n_customer=Customers(cid=cid,payment_dets=payment_Dets)
        n_customer.save()
        status['stat']='success'
    except:
        status['stat']='fail'
    return status
        


def order(data):
    status= {}
    try:
        search_element=data.POST['Shop_name']
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        c_id=u.values('uid')
        a=Users.objects.filter(Vendor__shop_name__exact=search_element)
        vid=a.values('uid')
        tnitem=data.POST['Number']
        dit=dict(data.order())

        temp=OrderDetails.object.latest('time')
        o_id=temp.values('oid')+1 # this to get the order id because order is autoincrement in order table but we need same order id for one order

        for i in range(tnitem+1):
            current_item="item_"+str(i+1)
            itm=json.load(dit[current_item])
            qty=itm['qty']
            iname=itm['name']
            icompany=itm['company']
            a=Items.objects.filter(item_name__exact=iname).filter(company__exact=icompany)
            cost=a.values('cost')
            iid=a.values('iid')
            t_cost=t_cost+(cost*qty) # to update total cost in orderdetail table

            order=Order(oid=o_id,iid=iid,qty=qty)
            order.save()

            s=Stock.object.filter(vid__exact=vid).filter(iid_exact=iid)
            s.units=s.values('units')-qty
            s.save()

        order_d=OrderDetails(oid=o_id,cid=c_id,vid=vid,time=datetime.now(),total_cost=t_cost)
        order_d.save()
        status['stat']='success'


    except:
        status['stat']="error"
        status['error']=traceback.format_exc()
    return status

def searchv(data):
    status= {}
    try:
        search_element=data.POST['Search_element']
        a=Users.objects.filter(Vendor__shop_name__contains=search_element)
        x=list(a.values('lat','lon','address','Vendor__shop_name','phno','Vendor__vid'))
        for i in range(len(x)):
            status[i]=x[i]
    except:
        status['stat']="error"
        status['error']=traceback.format_exc()
    print(status)
    return status

def view_vendor(data):
    status={}
    try:
        vendor_id=data.POST['Vid']
        if data.POST['action']=="Description":
            d=Vendor.objects.filter(Vendor__vid=vendor_id)
            des=d.values('description')
            status['returns']=des


        elif data.headers.get('action')=="Reviews":
            d=ReviewsRating.objects.filter(vid__exact=vendor_id)
            reviews=[]
            cnt=d.count()
            review=[]
            rev=list(d.values('review','rating'))
            cids=list(d.values('cid'))
            for i in range(cnt):
                n=Users.object.filter(uid__exact=cids[i])
                fnm = n.values('fname')
                mnm = n.values('mname')
                lnmn = n.values('lname')
                reviews.append([fnm,mnm,lnmn,rev[i][0],rev[i][1]])
            status['returns']=reviews

        elif data.headers.get('action')=="Items":
            it=Stock.objects.filter(vid__exact=vendor_id)
            cnt=it.count()
            retitems=[]
            item_cost=list(it.values('cost'))
            tem=list(it.values('iid'))
            for i in range(cnt):
                em=Items.object.filter(iid__exact=tem[i])
                item_details=list(em.values())
                retitems.append(tem[i],item_details,item_cost[i])
            status['returns']=retitems

            
    except:
        status['stat']="error"
        status['error']=traceback.format_exc()
    return status
    
def corderview(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uid=u.values('uid')
        order=OrderDetails.objects.filter(cid__exact=uid)
        o_list=list(order.values('oid','cid','time','did','paymnt_method','order_stat','total_cost'))
        for i in range(len(o_list)):
            detail={}
            v=Vendor.object.filter(vid__exact=o_list[i]['vid'])
            ven=list(v.values('Shop_Name'))
            vendor_name=ven[0]['Shop_Name']
            item_detail=order.object.filter(oid__exact=o_list[i]['oid'])
            item_detail_list=list(item_detail.values())
            item_res={'items':[],'qty':[],'cost':[]}
            for j in range(len(item_detail_list)):
                temp=Items.object.filter(iid__exact=item_detail_list[j]['iid'])
                l=list(temp.values('Item_Name','Cost','qty'))
                item_res['items'].append(l[0]['Item_Name'])
                item_res['qty'].append(item_detail_list[j]['qty'])
                item_res['cost'].append(l[0]['Cost'])

            detail['items']=item_res
            detail['v_name']=vendor_name
            detail['order_id']=o_list[i]['oid']
            detail['customer_id']=o_list[i]['cid']
            detail['time']=o_list[i]['time']
            detail['delivery_id']=o_list[i]['did']
            detail['paymnt_method']=o_list[i]['paymnt_method']
            detail['status']=o_list[i]['order_stat']
            detail['total_cost']=o_list[i]['total_cost']
            status[i]=detail
    except :
        status['stat']="Some error ocurred"
    return status

def Mon_order(data):
    status={}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        tnit=data.POST['Items_Count']
        uid=list(u.values('uid'))[0]['uid']
        shp_name=data.POST['Shop_Name']
        q=MonthlyOrder()
        q.cid=uid
        q.vid=list(Vendor.objects.filter(shop_name__exact=shp_name).values())[0]['shop_name']
        q.total_cost=0
        q.save()
        for i in range(tnit):
            x=Morder()
            current_item="Item_"+str(i+1)
            qwerty=data.POST[current_item]
            QWERTY=json.load(qwerty)
            o=order()
            o.iid=list(Items.objects.filter(item_name__exact=QWERTY['item_name']).filter(company__exact=QWERTY['item_company']).values('iid'))[0]['iid']
            o.qty=QWERTY['qty']
            o.save()

    except :
        status['stat']="error"
        traceback.print_exc()
    return status

def view_Mon_order(data):
    status={}
    try:

    except :
        status['stat']="error"
        traceback.print_exc() 
#         _            _            _      
#        /\ \         /\ \         /\ \    
#       /  \ \       /  \ \       /  \ \   
#      / /\ \ \     / /\ \ \     / /\ \ \  
#     / / /\ \_\   / / /\ \ \   / / /\ \_\ 
#    / /_/_ \/_/  / / /  \ \_\ / /_/_ \/_/ 
#   / /____/\    / / /   / / // /____/\    
#  / /\____\/   / / /   / / // /\____\/    
# / / /______  / / /___/ / // / /          
#/ / /_______\/ / /____\/ // / /           
#\/__________/\/_________/ \/_/            
                                    