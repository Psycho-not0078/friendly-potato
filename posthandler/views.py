from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import *
import datetime 
from .functions import *
# Create your views here.

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
                elif headder=="...":
                    response=asdfg()
                
            

        res=HttpResponse(response)
        

        #print(type(a[0]['tt']))
        return res
        #return HttpResponse("yooo!!")
