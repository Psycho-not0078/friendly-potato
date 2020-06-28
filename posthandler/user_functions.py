from django.http import HttpResponse
from .models import *
import os
from Crypto.Cipher import AES
from datetime import datetime;
from datetime import timedelta,timezone;
import traceback
import base64

def APIgen(uid):#working
    key = os.urandom(16)
    iv = os.urandom(AES.block_size)  
    #print(AES.block_size)
    #print(iv)
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

def APIfunct(data,string1):#working
    status={}
    headder=string1
    if(headder=="Sign_In"):
        status=sign_in(data)
    elif(headder=="Sign_Up"):
        status=sign_up(data)
    elif(headder=="Verify_acc"):
        status=uverify(data)
    return status

def verify(data):#working
    status= {}
    try:

        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        print(u.values())
        ptext=base64.b64decode(u.values('pt')[0]['pt'])
        key=base64.b64decode(u.values('api_key')[0]['api_key'])
        iv=base64.b64decode(u.values('iv')[0]['iv'])
        mode = AES.MODE_CBC
        cipher = AES.new(key, mode ,iv)
        hash=cipher.decrypt(base64.b64decode((data.META.get('HTTP_CIPHER'))))

        time_old=u.values('updated_time')[0]['updated_time']

        if(base64.b64encode(hash).decode('utf-8')==base64.b64encode(ptext).decode('utf-8')):
            time_10mins=timedelta(minutes=10)

            f=(datetime.now(timezone.utc)-time_old)
            '''print(f)
            print()'''
            if (abs(f/timedelta(minutes=1))<(10*60)):#condition to check time pased
                user=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
                user.update(updated_time=datetime.now())
                status['resp']="success"
                status['status']='verified'
            else:
                status['hash']=renew(data)
                if(status['hash']=='fail'):
                    del status['hash']
                    status['resp']="fail"
                    #print(status)
                else:
                    status['resp']="success"
                    status['stat']="renewed"
                    #print(status)
        else:
            status['resp']="fail"
            status['stat']=r"nah not going to happen --\(>_<)/--"
    except:
        #print("fail")
        status['stat']='fail'
        status['resp']="fail"
        #status['error']=traceback.format_exc()
        traceback.print_exc()
    return status

def renew(data):#working
    status=""
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        hash=APIgen(list(u.values('uid'))[0]['uid'])
        status=hash.decode("utf-8")
        #print(status)
    except:
        status='fail'
    return status

def sign_in(data):#working
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uco=u.count()
        if(uco==1):
            u.update(online=True)
            p=u.values('uid')[0]['uid']
            hash=APIgen(p)
            status['stat']="success"
            status['hash']=hash.decode("utf-8")
            

            
            #stat['resp']="skip"
        else:
            status['stat']="wrong_login"
            #stat['resp']="skip"
    except:
        status['stat']="error"
        #status['error']=traceback.format_exc()

    return status

def sign_up(data):#working
    status= {}
    try:
        #print("fuyu")
        user=Users()
        #print(list(Users.objects.all().values()))
        user.usrname=data.POST['Username']
        user.passwd=data.POST['Password']
        user.phno=data.POST['Phone_no']
        user.email_id=data.POST['Email_Id']
        user.fname=data.POST['Fname']
        user.mname=data.POST['Mname']
        user.lname=data.POST['Lname']
        user.type=data.POST['Type']
        user.online=True
        user.date_of_join=datetime.now()
        user.verified=0
        user.iv=0
        user.pt=" "
        user.api_key=" "
        user.iv=" "
        user.verified=False
        user.save()
        if(data.POST['Type']=="customer"):
            c=Customers()
            c.cid=user
            c.balance=0.0
            c.payment_dets=""
            c.save()
        elif(data.POST['Type']=="vendor"):
            v=Vendor()
            v.vid=user
            v.shop_name=" "
            v.gst_code=" "
            v.save()
        
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
        traceback.print_exc()
        #status['error']=traceback.format_exc()

    return status

def edit_profile(data):#working
    status= {}
    try:
        print("fuyu")
        user=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        #uid=u.values('uid')
        #user=Users.objects.filter(uid__exact=uid)
        #print(data.POST)
        dt=dict(data.POST)
        #print(dt)
        #print(dt['Phno'])
        #print(dt['Phno'][0])
        if(dt['Phno']):
            Phno=dt['Phno'][0]
            print(Phno)
            user.update(phno=Phno)
        if(dt['Email_Id'][0]):
            Email_Id=dt['Email_Id'][0]
            user.update(email_id=Email_Id)
        if(dt['Fname']):
            Fname=dt['Fname'][0]
            user.update(fname=Fname)
        if(dt['Mname']):
            Mname=dt['Mname'][0]
            user.update(mname=Mname)
        if(dt['Lname']):
            Lname=dt['Lname'][0]
            user.update(lname=Lname)
        if(dt['Address']):
            Address=dt['Address'][0]
            user.update(address=Address)

        #user.save()

        status['stat']="success"
    except :
        status['stat']="fail"
        #status['error']=traceback.format_exc()
        #traceback.print_exc()
    #print(status)
    return status

def sign_out(data):#working
    status= {}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        uco=u.filter(online=True).count()
        if(uco==1):
            u.update(online=False)
            status['stat']="success"
            #stat['resp']="skip"
        else:
            status['stat']="Nice Try"
            #stat['resp']="skip"
    except:
        status['stat']="error"
        #status['error']=traceback.format_exc()

    return status

def uverify(data):
    status={}
    try:
        u=Users.objects.filter(usrname__exact=data.META.get('HTTP_USERNAME')).filter(passwd__exact=data.META.get('HTTP_PASSWORD'))
        u.update(verified=True)
        status['stat']="success"
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
                                    