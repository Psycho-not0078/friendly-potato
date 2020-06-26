from datetime import datetime;
from datetime import timedelta,timezone;
import traceback
import base64
from .models import *
import os

def daily_cron_job(){
    m=MonthlyOrder.objects.values()
    try:
        dic=dict(m)
        for i in range(m.count()):
            a=OrderDetails()
            a.cid=dic[i]['cid']
            a.vid=dic[i]['vid']
            a.paymnt_method="Cash"
            a.order_stat="Ongoing"
            a.total_cost=0
            a.save()
    except:
        traceback.print_exc()
}