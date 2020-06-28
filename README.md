# friendly-potato
example of a django server for a serving APIs 

The APIs are for a system of customer/vendor apps ,the following tasks are now possible:
1. Sign in
2. Sign up
3. Order
4. Review
5. Stock taking
6. Monthly orders
and more.<br/>
This server would accept only post requests.
the server has a Api Auth system in place 

->The Common User Function are in user_functions.py<br/>
->The Vendor Functions are in vendor_functions.py<br/>
->The Customer Functions are in customer_functions.py<br/>
->There is a cron-job example in daily_cron.py, its nessary settings is in settings.py<br/>


# Procedure:
1. Execute the sql script named as homestop.sql
2. Create a user in the sql cl with the credintials as the one mentioned in the settings.py 
3. Update the port setting in settings.py
4. Check the nessary port fowarding settings
2. Execute init.sh for the first time
3. For the subcequent runs just running runserver.sh is enough

peace
