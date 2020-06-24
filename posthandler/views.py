from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from .models import * #the database connect
import datetime 
from .functions import *
from .userfunct import *
from .customer import *
from django.utils import *
import json

def index(request):
    if request.method=="POST":
        data=request.POST.copy()
        response={}
        headder=request.META.get('HTTP_ACTION')
        #print(headder)
        #print(type(headder))
        if(headder=="Sign_In" or headder=="Sign_Up"):
            print(asdfg)
            response=APIfunct(request,headder)
        else:
            stat=verify(request)
            print (stat)
            if(stat['resp']=="success"):
                if headder=="review":
                    response=review(request)
                if headder=='Search_Vendor':
                    response=searchv(request)
                if headder=='Locate':
                    response=locate(request)
                if headder=='Customer_View_Order':
                    response=corderview(request)
                if headder=='Vendor_View_Order':
                    response=vorderview(request)
                if headder=='Order_Place':
                    response=order(request)    
                if headder=='':
                    response=(request)
                elif headder=="...":
                    response=asdfg()
                
            
        res=JsonResponse(response)
        print(res.content)
        #res['cipher']=response['hash']#the string used for api authication

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
                                          