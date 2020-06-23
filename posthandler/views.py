from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import * #the database connect
import datetime 
from .functions import *
from .userfunct import *
from .customer import *


def index(request):
    if request.method=="POST":
        data=request.POST.copy()
        response={}
        headder=data.get('Action')
        if(headder=="Sign_In" or headder=="Sign_Up"):
            response=APIfunct(data)
        else:
            stat={}
            stat=verify(data.copy)
            if(stat['resp']=="success"):
                if headder=="review":
                    response=review(data)
                if headder=='Search_Vendor':
                    response=searchv(data)
                if headder=='Locate':
                    response=locate(data)
                if headder=='Customer_View_Order':
                    response=corderview(data)
                if headder=='Vendor_View_Order':
                    response=vorderview(data)
                if headder=='Order_place':
                    response=order(data)    
                if headder=='':
                    response=(data)
                elif headder=="...":
                    response=asdfg()
                
            
        res=HttpResponse(response)
        #res['cipher']=response['hash']#the string used for api authication
        print(response)

        #print(type(a[0]['tt']))
        return res
        #return HttpResponse("yooo!!")
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
                                          