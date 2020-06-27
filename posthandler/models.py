# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chat(models.Model):
    cid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='Cid', primary_key=True)  # Field name made lowercase.
    vid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vid')  # Field name made lowercase.
    msg = models.TextField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Chat'
        unique_together = (('cid', 'vid'),)


class DeliveryPersonal(models.Model):
    did = models.OneToOneField('Users', models.DO_NOTHING, db_column='Did', primary_key=True)  # Field name made lowercase.
    acc_dets = models.TextField(db_column='ACC_dets')  # Field name made lowercase.
    licence_no = models.CharField(db_column='Licence_no', unique=True, max_length=30)  # Field name made lowercase.
    licence_plt_no = models.CharField(db_column='Licence_plt_no', unique=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delivery_personal'


class MonthlyOrder(models.Model):
    mid = models.AutoField(db_column='Mid', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='Cid')  # Field name made lowercase.
    vid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vid')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    status = models.CharField(max_length=30)
    costpermonth = models.FloatField(db_column='CostPerMonth')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Monthly_Order'


class Morder(models.Model):
    moid = models.OneToOneField(MonthlyOrder, models.DO_NOTHING, db_column='Moid', primary_key=True)  # Field name made lowercase.
    iid = models.ForeignKey('Items', models.DO_NOTHING, db_column='iid')
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Morder'
        unique_together = (('moid', 'iid'),)


class Stock(models.Model):
    vid = models.OneToOneField('Vendor', models.DO_NOTHING, db_column='Vid', primary_key=True)  # Field name made lowercase.
    iid = models.ForeignKey('Items', models.DO_NOTHING, db_column='iid')
    cost = models.FloatField()
    units = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Stock'
        unique_together = (('vid', 'iid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customers(models.Model):
    cid = models.OneToOneField('Users', models.DO_NOTHING, db_column='Cid', primary_key=True, related_name="user", related_query_name="user")  # Field name made lowercase.
    payment_dets = models.TextField(db_column='Payment_Dets', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Items(models.Model):
    iid = models.IntegerField(primary_key=True)
    item_name = models.CharField(db_column='Item_Name', max_length=30)  # Field name made lowercase.
    company = models.IntegerField(db_column='Company')  # Field name made lowercase.
    cost = models.BigIntegerField(db_column='Cost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'items'


class Order(models.Model):
    oid = models.OneToOneField('OrderDetails', models.DO_NOTHING, db_column='oid', primary_key=True)
    iid = models.ForeignKey(Items, models.DO_NOTHING, db_column='iid')
    qty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'order'
        unique_together = (('oid', 'iid'),)


class OrderDetails(models.Model):
    oid = models.AutoField(db_column='Oid', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='cid')
    vid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='vid')
    time = models.DateTimeField()
    did = models.ForeignKey(DeliveryPersonal, models.DO_NOTHING, db_column='did', blank=True, null=True)
    paymnt_method = models.CharField(max_length=30)
    order_stat = models.CharField(max_length=10)
    total_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'order_details'


class ReviewsRating(models.Model):
    cid = models.OneToOneField(Customers, models.DO_NOTHING, db_column='cid', primary_key=True)
    vid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='vid')
    review = models.TextField()
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reviews_rating'
        unique_together = (('cid', 'vid'),)


class UserVerification(models.Model):
    uid = models.OneToOneField('Users', models.DO_NOTHING, db_column='uid', primary_key=True)
    email = models.CharField(max_length=30)
    hash = models.CharField(unique=True, max_length=100)
    time = models.DateTimeField()
    stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_verification'


class Users(models.Model):
    uid = models.AutoField(db_column='Uid', primary_key=True)  # Field name made lowercase.
    usrname = models.CharField(db_column='Usrname', unique=True, max_length=30)  # Field name made lowercase.
    passwd = models.TextField(db_column='Passwd')  # Field name made lowercase.
    phno = models.CharField(db_column='Phno', unique=True, max_length=15)  # Field name made lowercase.
    email_id = models.TextField(db_column='Email_Id', unique=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=30)  # Field name made lowercase.
    mname = models.CharField(db_column='Mname', max_length=30)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=30)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='Lon', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    online = models.IntegerField(db_column='Online')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    date_of_join = models.DateTimeField(db_column='date of join')  # Field renamed to remove unsuitable characters.
    pt = models.TextField()
    api_key = models.TextField()
    iv = models.TextField()
    updated_time = models.DateTimeField()
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Vendor(models.Model):
    vid = models.OneToOneField(Users, models.DO_NOTHING, db_column='Vid', primary_key=True, related_name="User", related_query_name="User")  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    gst_code = models.CharField(db_column='GST_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    acc_dets = models.TextField(db_column='ACC Dets', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shop_name = models.CharField(db_column='Shop_Name', max_length=30)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendor'
