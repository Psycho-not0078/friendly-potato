from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from .models import * #the database connect
import datetime 
from .vendor_functions import *
from .user_functions import *
from .customer_functions import *
from django.utils import *
import json#for sending the response in json for cross patform usage

def index(request):
    if request.method=="POST":
        data=request.POST.copy()
        response={}
        headder=request.META.get('HTTP_ACTION')
        #print(headder)
        #print(type(headder))
        if(headder=="Sign_In" or headder=="Sign_Up"):#working
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
                if headder=='Stock':
                    response=stock(request)
                if headder=='Order_Place':
                    response=order(request)    
                if headder=='Edit_Profile':#working   
                    response=edit_profile(request)
                    #print(response)
                elif headder=="":
                    response=asdfg()
                elif headder=="Sign_Out":
                    response=sign_out(request)
                elif headder=="Verify":
                    response=uverify(request)
            response.update(stat)
            del response['resp']
        #print(response)
        res=JsonResponse(response , safe=False)
        #print(res.content)

        return res
        #return HttpResponse("yooo!!")#first response of nothing (>_<)
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
                                          