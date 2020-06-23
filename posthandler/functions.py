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


def asdfg():
    status=[]
    status.append(".__                    .__         .__  .__  _____    _________    __                               .__                   __  .__                                              .__               ")
    status.append("|  |__   ______  _  __ |__| ______ |  | |__|/ ____\___\_____   \ _/  |________ ___.__.  __ __  _____|__| ____    ____   _/  |_|  |__   ____   _____  ______ ______        ____ |__|____    ____  ")
    status.append("|  |  \ /  _ \ \/ \/ / |  |/  ___/ |  | |  \   __\/ __ \ /   __/ \   __\_  __ <   |  | |  |  \/  ___/  |/    \  / ___\  \   __\  |  \_/ __ \  \__  \ \____ \\____ \     _/ ___\|  \__  \  /  _ \ ")
    status.append("|   Y  (  <_> )     /  |  |\___ \  |  |_|  ||  | \  ___/|   |     |  |  |  | \/\___  | |  |  /\___ \|  |   |  \/ /_/  >  |  | |   Y  \  ___/   / __ \|  |_> >  |_> >    \  \___|  |/ __ \(  <_> )")
    status.append("|___|  /\____/ \/\_/   |__/____  > |____/__||__|  \___  >___|     |__|  |__|   / ____| |____//____  >__|___|  /\___  /   |__| |___|  /\___  > (____  /   __/|   __/ /\   \___  >__(____  /\____/ ")
    status.append("     \/                        \/                     \/<___>                  \/                 \/        \//_____/              \/     \/       \/|__|   |__|    \/       \/        \/        ")
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

def stock(data):
    status={}
    try:
        v=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        Vid=v.values('vid')
        tnitem=data['Number']
        dit=dict(data.items())
        for i in range(tnitem):
            current_item="Item_"+str(i)
            qty=dit[current_item][2]
            iname=dit[current_item][0]
            icompany=dit[current_item][1]
            a=Items.objects.filter(item_name__exact=iname).filter(company__exact=icompany)
            if(a.count()!=1):
                d=Items(name=iname,company=icompany,description=dit[current_item][3])
                d.save()
            s=Stock(vid=Vid,iid=a.values('iid'),units=qty)
            s.save()
        status['stat']='success'
    except :
        status['stat']='error'
    return status


def view_vendor(data):
    status={}
    try:
        vendor_id=data['Vid']
        d=Users.objects.filter(Vendor__vid=vendor_id)
        x=list(a.values('Vendor__vid','Vendor'))
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

def vorderview(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        vid=u.values('uid')
        order=OrderDetails.objects.filter(vid__exact=vid)
        order_list=list(order.values('oid','cid','time','did','paymnt_method','order_stat','total_cost'))
        for i in range(len(order_list)):
            detail={}
            ven=user.object.filter(vid__exact=order_list[i]['cid'])
            user=list(v.values('Usrname'))
            user_name=ven[0]['Usrname']
            item_detail=ord.object.filter(oid__exact=order_list[i]['oid'])#selet * into #temp from ord where oid=oid
            item_detail_list=list(item_detail.values('iid'))#selet * from #temp      select iid from temp
            item_res={'items':[],'qty':[],'cost':[]}
            for j in range(len(item_detail_list)):
                temp=items.object.filter(iid__exact=item_detail_list[j])
                l=list(temp.values())
                item_res['items'].append(l[0]['Item_Name'])
                item_res['qty'].append(item_detail_list[j]['qty'])
                item_res['cost'].append(l[0]['Cost'])

            detail['items']=item_res
            detail['u_name']=user_name
            detail['order_id']=order_list[i]['oid']
            detail['customer_id']=order_list[i]['cid']
            detail['time']=order_list[i]['time']
            detail['delivery_id']=order_list[i]['did']
            detail['paymnt_method']=order_list[i]['paymnt_method']
            detail['status']=order_list[i]['order_stat']
            detail['total_cost']=order_list[i]['total_cost']
            status[i]=detail
    except :
        status['stat']="Some error ocurred"
    return status


def locate(data):
    status= {}
    try:
        search_element1=data['Fname']
        search_element2=data['Mname']
        search_element3=data['Lname']
        a=Users.objects.filter(fname__exact=search_element1).filter(mname__exact=search_element2).filter(lname__exact=search_element3)
        x=list(a.values('lat','lon','address','phno',))
        for i in range(len(x)):
            status[i]=x[i]
    except:
        status['stat']="error"
    return status



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
                                          