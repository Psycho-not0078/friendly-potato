from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta;


def review(data):
    status={}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        uid=u.values('uid')
        v=Users.objects.filter(Vendor__shop_name=data['Shop_name'])
        vid=u.values('vid')
        review=data['Review']
        ratings=data['Rating']
        rev=ReviewsRating(cid=uid,vid=vid,review=review,rating=ratings)
        rev.save()
        status['stat']="success"
    except:
        status['stat']="fail"

    return status


def order(data):
    status= {}
    try:
        search_element=data['Shop_name']
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        c_id=u.values('uid')
        a=Users.objects.filter(Vendor__shop_name__exact=search_element)
        vid=a.values('uid')
        order=data['order']
        items=order['item_name']
        quantity=order['qty']
        item_iid=[]
        item_cost=[]
        t_cost=0;
        for i in range(len(quantity)):
            t_cost=t_cost+(item_cost[i]*quantity[i])

        t2=OrderDetails(cid=c_id,vid=vid,total_cost=t_cost)
        t2.save()
        temp=OrderDetails.object.latest('time')
        o_id=temp.values('oid')
        for i in items:
            temp=items.object.filter(Item_Name__exact=i)
            i_id=temp.values('iid')
            i_cost=temp.values('cost')
            item_iid.append(i_id)
            item_cost.append(i_cost)
        

        for i in range(len(item_iid)):
            t1=Order(oid=o_id,iid=item_iid[i],qty=quantity[i])
            t1.save()

        t2=OrderDetails(oid=o_id,cid=c_id,vid=vid,total_cost=t_cost)
        t2.save()

        for i in range(len(item_iid)):
            s=Stock.object.filter(vid__exact=vid).filter(iid_exact=item_iid[i])
            s.units=s.values('units')-quantity[i]
            s.save()

    except:
        status['stat']="error"
    return status

def searchv(data):
    status= {}
    try:
        search_element=data['Search_element']
        a=Users.objects.filter(Vendor__shop_name__contains=search_element)
        x=list(a.values('lat','lon','address','Vendor__shop_name','phno','Vendor__vid'))
        for i in range(len(x)):
            status[i]=x[i]
    except:
        status['stat']="error"
    return status

def view_vendor(data):
    status=[]
    try:
        vendor_id=data['Vid']
        d=Users.objects.filter(Vendor__vid=vendor_id)
        x=dict(d.values('Vendor__vid','Vendor__Shop_name','address'))
        status=x
    except:
        status['stat']="error"
    return status
    
def corderview(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
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
                temp=items.object.filter(iid__exact=item_detail_list[j]['iid'])
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