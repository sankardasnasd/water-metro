from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)




class Boat(models.Model):
    # USER = models.ForeignKey(User,on_delete=models.CASCADE)
    boatname = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)


class Metro_Station(models.Model):
    # USER = models.ForeignKey(User, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Metro_Service(models.Model):
    BOAT = models.ForeignKey(Boat, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    fromplace = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)


class Schedule(models.Model):
    BOAT = models.ForeignKey(Boat, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    fromplace = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)


class Bank(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    IFSC = models.CharField(max_length=100)
    paydate = models.CharField(max_length=100)
    paystatus = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)







class Booking(models.Model):
    SCHEDULE = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    totalticket = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)



class Otp(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    otp = models.CharField(max_length=100)
    sent_time = models.CharField(max_length=100)
    expiredate = models.CharField(max_length=100)



class Payment(models.Model):
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # otp = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Complaint(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    # otp = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=100)