from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta;
import json
import traceback

def asdfg():
    status=[]
    status.append(".__                    .__         .__  .__  _____    _________    __                               .__                   __  .__                                              .__               ")
    status.append("|  |__   ______  _  __ |__| ______ |  | |__|/ ____\___\_____   \ _/  |________ ___.__.  __ __  _____|__| ____    ____   _/  |_|  |__   ____   _____  ______ ______        ____ |__|____    ____  ")
    status.append("|  |  \ /  _ \ \/ \/ / |  |/  ___/ |  | |  \   __\/ __ \ /   __/ \   __\_  __ <   |  | |  |  \/  ___/  |/    \  / ___\  \   __\  |  \_/ __ \  \__  \ \____ \\____ \     _/ ___\|  \__  \  /  _ \ ")
    status.append("|   Y  (  <_> )     /  |  |\___ \  |  |_|  ||  | \  ___/|   |     |  |  |  | \/\___  | |  |  /\___ \|  |   |  \/ /_/  >  |  | |   Y  \  ___/   / __ \|  |_> >  |_> >    \  \___|  |/ __ \(  <_> )")
    status.append("|___|  /\____/ \/\_/   |__/____  > |____/__||__|  \___  >___|     |__|  |__|   / ____| |____//____  >__|___|  /\___  /   |__| |___|  /\___  > (____  /   __/|   __/ /\   \___  >__(____  /\____/ ")
    status.append("     \/                        \/                     \/<___>                  \/                 \/        \//_____/              \/     \/       \/|__|   |__|    \/       \/        \/        ")
    return status

def stock(data):
    status={}
    try:
        v=Users.objects.get(usrname__exact=data.META.get('HTTP_USERNAME'))
        #Vid=v.values('Vendor_vid')
        tnitem=data.POST['Number']
        print(data.POST['Number'])
        dit=dict(data.items())
        print(dit)
        for i in range(tnitem+1):
            current_item="Item_"+str(i+1)
            itm=json.load(dit[current_item])
            qty=itm['qty']
            iname=itm['name']
            icompany=itm['company']
            a=Items.objects.filter(item_name__exact=iname).filter(company__exact=icompany) 
            if(a.count()!=1):
                desctiption=itm['description']
                d=Items(name=iname,company=icompany,description=desctiption)
                d.save()
            else:
                d=Items.objects.get(a.values('iid')[0]['iid'])
            s=Stock(vid=v,iid=a,units=qty)
            s.save()
        status['stat']='success'
    except :
        status['stat']='error'
        traceback.print_exc()
    return status

def vorderview(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        vid=u.values('uid')
        order=OrderDetails.objects.filter(vid__exact=vid)
        order_list=list(order.values('oid','cid','time','did','paymnt_method','order_stat','total_cost'))
        for i in range(len(order_list)):
            detail={}
            ven=user.objects.filter(vid__exact=order_list[i]['cid'])
            user=list(ven.values('Usrname'))
            user_name=ven[0]['Usrname']
            item_detail=order.objects.filter(oid__exact=order_list[i]['oid'])#selet * into #temp from ord where oid=oid
            item_detail_list=list(item_detail.values('iid'))#selet * from #temp      select iid from temp
            item_res={'items':[],'qty':[],'cost':[]}
            for j in range(len(item_detail_list)):
                temp=Items.objects.filter(iid__exact=item_detail_list[j])
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
        search_element1=data.POST['Fname']
        search_element2=data.POST['Mname']
        search_element3=data.POST['Lname']
        a=Users.objects.filter(fname__exact=search_element1).filter(mname__exact=search_element2).filter(lname__exact=search_element3)
        x=list(a.values('lat','lon','address','phno',))
        for i in range(len(x)):
            status[i]=x[i]
    except:
        status['stat']="error"
        traceback.print_exc()
    return status

def set_details(data):
    status={}
    try:
        '''v=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        vid=v.values('uid')[0]['uid']'''
        description=data.POST["description"]
        gst_code=data.POST["GST_code"]
        acc_details=data.POST["acc_details"]
        shop_name=data.POST["shop_name"]
        #print(Vendor.objects.all().values('vid'))
        n_vendor=Vendor.objects.filter(vid__usrname__exact=data.META.get('HTTP_USERNAME'),vid__passwd__exact=data.META.get('HTTP_PASSWORD'))
        n_vendor.update(description=description)
        n_vendor.update(gst_code=gst_code)
        n_vendor.update(shop_name=shop_name)
        status['stat']='success'
    except:
        status['stat']='fail'
        traceback.print_exc()
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
                                          