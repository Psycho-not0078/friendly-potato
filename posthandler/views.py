from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import * #the database connect
import datetime 
from .functions import *


def index(request):
    if request.method=="POST":
        data=request.POST.copy()
        response={}
        headder=data.headers.get('Action')
        if(headder=="Sign_in" or headder=="Sign_up"):
            response=APIfunct(data.copy())
        else:
            stat={}
            stat=verify(data.copy)
            if(stat['resp']=="success"):
                if headder=="review":
                    response=review(data.copy())
                if headder=='Search_Vendor':
                    response=searchv(data.copy())
                if headder=='Locate':
                    response=locate(data.copy())
                if headder=='Customer_View_Order':
                    response=corderview(data.copy())
                if headder=='Vendor_View_Order':
                    response=vorderview(data.copy())
                if headder=='Order_place':
                    response=order(data.copy())    
                if headder=='':
                    response=(data.copy())

                elif headder=="...":
                    response=asdfg()
                
            

        res=HttpResponse(response)
        res['cipher']=response['hash']#the string used for api authication
        

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
                                          