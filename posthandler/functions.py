from django.http import HttpResponse
from .models import *
import os
from.AEScipher import AESCipher


def APIfunct(data):
    headdder=data.headers.get('Action')
    if(headdder=="Sign_Up"):
        status=HttpResponse(sign_in(data))
    elif(headdder=="Sign_In"):
        status=HttpResponse(sign_up(data))
    return status

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

    return "null"

def verify(data):
    status= {}
    return status

def renew(data):
    status= {}
    return status

def sign_in(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        uco=u.count()
        if(uco==1):
            hash=APIgen(u.values('email'),u.values('uid'))
            status['hash']=hash
        else:
            status['stat']="wrong_login"
    except:
        status['stat']="error"

    return status

def APIgen(string,uid):
    key=os.urandom(256)
    c=AESCipher(key)
    encstr=c.encrypt(string)

    c=Users.objects.filter(uid__exact=uid).update(api_key=key)
    return encstr


def sign_up(data):
    status= {}
    return status

def order():
    status= {}
    return status

def searchv(data):
    status= {}
    try:
        search_element=data['Search_element']
        a=Users.objects.filter(Vendor__shop_name__contains=search_element)
        x=list(a.values())
        for i in range(len(x)):
            status[i]=x[i]
    except:
        status['stat']="error"
    return status

def corderview():
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        uid=u.values('uid')
        order=order_details.objects.filter(cid__exact=uid)
        o=list(order.values())
        for i in range(len(o)):
            detail={}
            v=vendor.object.filter(vid__exact=o[i]['vid'])
            ven=list(v.values())
            vendor_name=ven[0]['Shop_Name']
            it=ord.object.filter(oid__exact=o[i]['oid'])
            items=list(it.values())
            item={'items':[],'qty':[],'cost':[]}
            for j in range(len(items)):
                temp=items.object.filter(iid__exact=items[j]['iid'])
                l=list(temp.values())
                item['items'].append(l[0]['Item_Name'])
                item['cost'].append(l[0]['Cost'])
                item['qty'].append(items[j]['qty'])

            detail['items']=item
            detail['v_name']=vendor_name
            detail['order_id']=o[i]['oid']
            detail['customer_id']=o[i]['cid']
            detail['time']=o[i]['time']
            detail['delivery_id']=o[i]['did']
            detail['paymnt_method']=o[i]['paymnt_method']
            detail['status']=o[i]['order_stat']
            detail['total_cost']=o[i]['total_cost']
            status[i]=detail
    except :
        status['stat']="Some error ocurred"
    return status

def vorderview():
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        vid=u.values('uid')
        order=order_details.objects.filter(vid__exact=vid)
        o=list(order.values())
        for i in range(len(o)):
            detail={}
            u=user.object.filter(vid__exact=o[i]['cid'])
            user=list(v.values())
            user_name=ven[0]['Usrname']
            it=ord.object.filter(oid__exact=o[i]['oid'])
            items=list(it.values())
            item={'items':[],'qty':[],'cost':[]}
            for j in range(len(items)):
                temp=items.object.filter(iid__exact=items[j]['iid'])
                l=list(temp.values())
                item['items'].append(l[0]['Item_Name'])
                item['cost'].append(l[0]['Cost'])
                item['qty'].append(items[j]['qty'])

            detail['items']=item
            detail['u_name']=user_name
            detail['order_id']=o[i]['oid']
            detail['customer_id']=o[i]['cid']
            detail['time']=o[i]['time']
            detail['delivery_id']=o[i]['did']
            detail['paymnt_method']=o[i]['paymnt_method']
            detail['status']=o[i]['order_stat']
            detail['total_cost']=o[i]['total_cost']
            status[i]=detail
    except :
        status['stat']="Some error ocurred"
    return status


def locate():
    status= {}
    return status

def edit_profile(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        uid=u.values('uid')
        user=Users.objects.filter(uid__exact=uid)
        if(data['Username']):
            Username=data['Username']
            user.Username=Username
        if(data['Phno']):
            Phno=data['Phno']
            user.Phno=Phno
        if(data['Email_Id']):
            Email_Id=data['Email_Id']
            user.Email_Id=Email_Id
        if(data['Fname']):
            Fname=data['Fname']
            user.Fname=Fname
        if(data['Mname']):
            Mname=data['Mname']
            user.Mname=Mname
        if(data['Lname']):
            Lname=data['Lname']
            user.Lname=Lname
        if(data['Address']):
            Address=data['Address']
            user.Address=Address

        user.save()

        status['stat']="success"
    except :
        status['stat']="fail"
    
    return status


