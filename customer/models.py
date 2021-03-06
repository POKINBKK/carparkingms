from django.contrib.auth.models import User
from django.db import models
# คนมีpointเพิ่ม
from django.utils.encoding import force_text


class Parking_zone(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    available = models.IntegerField()
    def __str__(self):
        return self.name

class Parking_slot(models.Model):
    status = models.BooleanField(null=False)
    parking_zone = models.ForeignKey(Parking_zone,models.PROTECT)
    reservation = models.ManyToManyField('Reservation')
    def __str__(self):
        return force_text(self.id)


class Parking(models.Model):
    arrive_at = models.DateField(null=True)
    leave_at = models.DateField(null=True)
    parking_zone = models.ForeignKey(Parking_zone, models.PROTECT)
    parking_slot = models.ForeignKey(Parking_slot, models.PROTECT)
    parking_token = models.CharField(max_length=255,null=True)



class User_sys(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    TYPES = (
        ('re', 'register_user'),
        ('gu', 'guess_user')
    )
    type = models.CharField(choices=TYPES,default='gu',max_length=2)
    def __str__(self):
        return force_text(self.user.username)

class Register_user(models.Model):
    phone_number = models.CharField(max_length=10)
    point = models.IntegerField()
    user = models.ForeignKey(User_sys, models.PROTECT)

    def __str__(self):
        return force_text(self.id)


class Reservation(models.Model):
    TYPES = (
        ('re', 'reserved'),
        ('ca', 'cancle')
    )

    reserve_status = models.CharField(choices=TYPES,default='re',max_length=2)
    reserve_token = models.CharField(max_length=64)
    reserve_at = models.DateField()
    point_use = models.IntegerField()
    register_user = models.ForeignKey(Register_user, models.PROTECT)


class Car(models.Model):
    register_user = models.ForeignKey(Register_user,models.PROTECT)
    car_license_number = models.CharField(primary_key=True ,max_length=25)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)

class Buypackage(models.Model):
    point_added = models.IntegerField(null=False)
    add_date = models.DateTimeField()
    user = models.ForeignKey(User,models.PROTECT)
# Create your models here.
# class Regist_user(models.Model):
#     username = models.CharField(max_length=255)
#     user_fname = models.CharField(max_length=255)
#     user_lname = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=10)
#     point = models.IntegerField()
#     user = models.ForeignKey(User_sys, models.PROTECT)
# class user(models.Model):
#     TYPES = (
#         ('re', 'register_user'),
#         ('gu', 'guess_user')
#     )
#     type = models.CharField(choices=TYPES, default='gu', max_length=2)