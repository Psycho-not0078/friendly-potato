# friendly-potato
django server for a serving APIs for homestop app

The APIs are for the following tasks:
1)sign in
2)sign up
3)order
4)review
5)stock
and more.
This server would accept only post requests.

Make sure that nessary port forwarding is enabled for the server to be accessed from multiple networks.

Procedure:
1.Install all libraries in requirements.txt
2.Change the server settings in settings.py,this includes the port for mysql or anyother database for that matter is is because the server's First task is to connect to the database
4.Execute the command python manage.py makemigrations
5.Execute the command python manage.py migrate
6.Execute the command python manage.py runserver

peace
