from django.http import HttpResponse
from .models import *
import os
from.AEScipher import AESCipher


def APIfunct(data):
    headdder=data.headers.get('Action')
    if(headdder=="Sign_Up"):
        status=HttpResponse(s9jign_in(data))
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
    user=Users(usrname=data['Username'],passwd=data['Password'],phno=data['Phone_no'],email_id=data['Email_Id'],type=data['Type'])
    user.save()
    return status

def order():
    status= {}
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
    status={}
    try:
        vendor_id=data['Vid']
        d=Users.objects.filter(Vendor__vid=vendor_id)
        x=list(a.values('Vendor__vid','Vendor'))
    except:
        status['stat']="error"
    return status
def corderview():
    status= {}
    try:
        pass
    except :
        pass
    return status

def vorderview():
    status= {}
    try:
        pass
    except :
        pass
    return status

def locate():
    status= {}
    return status

