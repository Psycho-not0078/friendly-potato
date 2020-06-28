from datetime import datetime;
from datetime import timedelta,timezone;
import traceback
import base64
from .models import *
import os

def daily_cron_job():
    m=MonthlyOrder.objects.all().values()
    try:
        dic=list(m)
        for i in range(m.count()):
            a=OrderDetails()
            a.cid=dic[i]['cid']
            a.vid=dic[i]['vid']
            a.paymnt_method="Cash"
            a.order_stat="Ongoing"
            a.total_cost=0
            a.save()

            mid=dic[i]['mid']
            for j in range(Morder.objects.filter(mid__exact=mid).count()):
                #oid=(list(OrderDetails.objects.latest('time').values('oid'))[0]['oid']+
                x=Order()
                x.oid=a
                qty=list(Morder.objects.filter(mid__exact=mid).values('qty'))[i]['qty']
                iid=Items.objects.get(iid=list(Morder.objects.filter(mid__exact=mid).values('iid'))[i]['iid'])
                x.qty=qty
                cst=qty*((list(Items.objects.filter(iid__exact=iid).values('cost')))[0]['cost'])
                x.iid=iid
                x.save()
                z=MonthlyOrder.objects.filter(mid__exact=mid)
                z.total_cost=z.total_cost+cst 
                if(list(Stock.objects.filter(vid__exact=dic[i]['cid']).filter(iid__exact=iid).values('units'))[0]['units']>0):
                    q=Stock.objects.filter(vid__exact=dic[i]['cid']).filter(iid__exact=iid)
                    q.units=q.units-qty
                else:
                    print("error_stock_not_updated")
    except:
        traceback.print_exc()
