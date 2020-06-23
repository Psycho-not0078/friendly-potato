from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta;


def APIfunct(data):
    headdder=data.headers.get('Action')
    if(headdder=="Sign_In"):
        status=sign_in(data)
    elif(headdder=="Sign_Up"):
        status=sign_up(data)
    return status

def verify(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        ptext=u.values('email')
        key=u.values('API_KEY')
        iv=u.values('iv')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        time_old=u.values('updated_time')
        time_10mins=timedelta(minutes=10)
        if(cipher.decrypt(data['cipher'])==ptext):
            if (datetime.now()-time_old<time_10mins):#condition to check time pased
                status['resp']=="success"
            else:
                status=renew(data)
                status['resp']=="success"
    except:
        status['stat']='fail'
    return status

def renew(data):
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        hash=APIgen(u.values('email'),u.values('uid'))
        status['hash']=hash
    except:
        status['stat']='fail'
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

def sign_up(data):
    status= {}
    try:
        user=Users(usrname=data['Username'],passwd=data['Password'],phno=data['Phone_no'],email_id=data['Email_Id'],type=data['Type'])
        user.save()
        Use=Users.objects.filter(usrname__exact=data['Username']).filter(passwd__exact=data['Password'])
        hash=APIgen(Use.values('email'),Use.values('uid'))
        status['hash']=hash
    except:
        status['stat']="error"
    return status

def APIgen(string,uid):
    key = os.urandom(16)
    iv = os.urandom(AES.block_size)      
    mode = AES.MODE_CBC
    cipher = AES.new(key,mode,iv)
    encstr=cipher.encrypt(string)
    ret=base64.b64encode(encstr)

    c=Users.objects.filter(uid__exact=uid).update(api_key=key)
    d=Users.objects.filter(uid__exact=uid).update(iv=iv)
    return ret

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
                                    