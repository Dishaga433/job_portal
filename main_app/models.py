from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_worker=models.BooleanField(default=False)
    is_employer=models.BooleanField(default=False)


class Worker(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Worker")
    Name=models.CharField(max_length=20)
    Age=models.CharField(max_length=3)
    DOB = models.DateField()
    Address=models.TextField()
    Ph_no=models.CharField(max_length=10)
    Job_category=models.CharField(max_length=50)
    Experience=models.CharField(max_length=30)
    Preffered_location=models.CharField(max_length=30)
    Job_type=(
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
        ('Contract','Contract'),
    )
    type = models.CharField(max_length=10, choices=Job_type)
    document = models.FileField(upload_to='documents/')





class Employer(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Employer")
    Name=models.CharField(max_length=20)
    Address=models.TextField()
    State=models.CharField(max_length=20)
    Ph_no=models.CharField(max_length=10)
    Email = models.EmailField()
    document = models.FileField(upload_to='documents/')



class Openings(models.Model):
    Employer_name = models.ForeignKey('Employer', on_delete=models.CASCADE)
    Job_title=models.CharField(max_length=30)
    Job_description=models.TextField()
    Place=models.CharField(max_length=20)
    wage=models.CharField(max_length=20)
    status = models.IntegerField(default=0)




class Request(models.Model):
    Worker_name = models.ForeignKey('Worker', on_delete=models.CASCADE)
    Employer_name = models.ForeignKey('Employer', on_delete=DO_NOTHING, blank=True, null=True)
    Age=models.CharField(max_length=3)
    DOB = models.DateField()
    Address=models.TextField()
    Ph_no=models.CharField(max_length=10)
    Job_category=models.CharField(max_length=50)
    Experience=models.CharField(max_length=30)
    Preffered_location=models.CharField(max_length=30)
    Job_type=(
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
        ('Contract','Contract'),
    )
    type = models.CharField(max_length=10, choices=Job_type)
    status = models.IntegerField(default=0)




class Feedback(models.Model):
    Worker_name=models.ForeignKey("Worker",on_delete=models.CASCADE)
    message=models.TextField()
    date=models.DateTimeField(auto_now=True)
    reply=models.CharField(max_length=200,null=True,blank=True)





class Employer_feed(models.Model):
    Employer_name=models.ForeignKey("Employer",on_delete=models.CASCADE)
    message=models.TextField()
    date=models.DateTimeField(auto_now=True)
    reply=models.CharField(max_length=200,null=True,blank=True)




