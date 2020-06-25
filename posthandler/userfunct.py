from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta,timezone;
import traceback
import base64


def APIfunct(data,string1):
    status={}
    headder=string1
    if(headder=="Sign_In"):
        status=sign_in(data)
    elif(headder=="Sign_Up"):
        status=sign_up(data)
    return status

def verify(data):
    status= {}
    try:
        print("running")
        #print(data.META.get('HTTP_USERNAME'))
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        ptext=base64.b64decode(u.values('pt')[0]['pt'])
        key=base64.b64decode(u.values('api_key')[0]['api_key'])
        iv=base64.b64decode(u.values('iv')[0]['iv'])
        mode = AES.MODE_CBC
        cipher = AES.new(key, mode ,iv)
        hash=cipher.decrypt(base64.b64decode((data.META.get('HTTP_CIPHER'))))
        print(type(key))
        #print(key)

        #print(data.META)
        print(base64.b64encode(hash).decode('utf-8'))
        print(base64.b64encode(ptext).decode('utf-8'))
        #print(data.META)
        time_old=u.values('updated_time')[0]['updated_time']
        time_10mins=timedelta(minutes=10)
        print("asdfghjk")
        if(base64.b64encode(hash).decode('utf-8')==base64.b64encode(ptext).decode('utf-8')):
            #print("asdg")
            if ((datetime.now(timezone.utc)-time_old)<time_10mins):#condition to check time pased
                print("still running")
                status['resp']="success"
            else:
                status=renew(data)
                print("nah")
                status['resp']="success"
        else:
            status['resp']=r"nah not going to happen --\(>_<)/--"
    except:
        print("fail")
        status['stat']='fail'
        status['resp']="fail"
        status['error']=traceback.format_exc()
    return status

def renew(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        hash=APIgen(u.values('uid'))
        status['hash']=hash
    except:
        status['stat']='fail'
    return status

def sign_in(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uco=u.count()
        if(uco==1):
            p=u.values('uid')[0]['uid']
            hash=APIgen(p)
            status['stat']="success"
            status['hash']=hash.decode("utf-8")
            

            u.update(online=True)
            #stat['resp']="skip"
        else:
            status['stat']="wrong_login"
            #stat['resp']="skip"
    except:
        status['stat']="error"
        status['error']=traceback.format_exc()

    return status

def sign_up(data):
    status= {}
    try:
        #print("fuyu")
        user=Users()
        user.usrname=data.POST['Username']
        user.passwd=data.POST['Password']
        user.phno=data.POST['Phone_no']
        user.email_id=data.POST['Email_Id']
        user.type=data.POST['Type']
        user.online=0
        user.date_of_join=datetime.now()
        user.verified=0
        user.iv=0
        user.pt=" "
        user.api_key=" "
        user.iv=" "
        user.save()
        Use=Users.objects.filter(usrname__exact=data.POST['Username']).filter(passwd__exact=data.POST['Password'])
        #print("fuyu")
        s=list(Use.values('uid'))
        #print(s)
        hash=APIgen(s[0]['uid'])
        status['stat']="success"
        status['hash']=hash.decode('UTF-8')
        #status['resp']="skip"
    except:
        status['stat']="error"
        status['error']=traceback.format_exc()

    return status

def APIgen(uid):
    key = os.urandom(16)
    iv = os.urandom(AES.block_size)  
    print(AES.block_size)
    print(iv)
    strings= os.urandom(AES.block_size)    
    mode = AES.MODE_CBC
    cipher = AES.new(key,mode,iv)
    encstr=cipher.encrypt(strings)
    ret=base64.b64encode(encstr)

    c=Users.objects.filter(uid__exact=uid)
    c.update(api_key=base64.b64encode(key).decode('UTF-8'))
    c.update(iv=base64.b64encode(iv).decode('UTF-8'))
    c.update(pt=base64.b64encode(strings).decode('UTF-8'))

    #c.save()

    return ret

def edit_profile(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uid=u.values('uid')
        user=Users.objects.filter(uid__exact=uid)
        if(data.POST['Username']):
            Username=data.POST['Username']
            user.Username=Username
        if(data.POST['Phno']):
            Phno=data.POST['Phno']
            user.Phno=Phno
        if(data.POST['Email_Id']):
            Email_Id=data.POST['Email_Id']
            user.Email_Id=Email_Id
        if(data.POST['Fname']):
            Fname=data.POST['Fname']
            user.Fname=Fname
        if(data.POST['Mname']):
            Mname=data.POST['Mname']
            user.Mname=Mname
        if(data.POST['Lname']):
            Lname=data.POST['Lname']
            user.Lname=Lname
        if(data.POST['Address']):
            Address=data.POST['Address']
            user.Address=Address

        user.save()

        status['stat']="success"
    except :
        status['stat']="fail"
    
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
                                    