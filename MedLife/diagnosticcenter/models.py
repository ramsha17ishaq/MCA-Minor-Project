from django.db import models
from django.utils import timezone

# Create your models here.

class Test_Detail(models.Model):
    Test_name = models.CharField(max_length=100,primary_key=True,null=False)
    Charge = models.IntegerField(null=False)
    Test_condition = models.CharField(max_length=100,null=False)

class Health_Campaign(models.Model):
    Campaign_Name = models.CharField(max_length=100,null=False)
    Organizer_name = models.CharField(max_length=45,null=False)
    Venue = models.CharField(max_length=50,null=False)
    Description = models.TextField()
    Date = models.DateField(default=timezone.now)

class Contact(models.Model):
    Name = models.CharField(max_length=45,null=False)
    Email = models.EmailField(max_length=45)
    Phone = models.CharField(max_length=10,null=False)
    Your_query=models.TextField()
    Date=models.DateField(default=timezone.now)

class FeedBack(models.Model):
    Name = models.CharField(max_length=45,null=False)
    Email = models.EmailField(max_length=45,null=False)
    Feedbacktext = models.TextField()
    Rating = models.IntegerField(default=1)
    Date = models.DateField(default=timezone.now)

class Job(models.Model):
    PostName = models.CharField(max_length=30,null=False)
    NoOfseats = models.IntegerField(null=False)
    Lastdatetoapply = models.DateField(default=timezone.now)
    Postdate = models.DateField(default=timezone.now)
    Description = models.TextField()

class Appointment(models.Model):
    Name = models.CharField(max_length=20,null=False)
    Phone = models.CharField(max_length=10,null=False)
    Email = models.EmailField(max_length=45)
    Test_name = models.CharField(max_length=100,null=False)
    Booking_Type = models.CharField(max_length=20,null=False)
    Date = models.DateField(default=timezone.now)




