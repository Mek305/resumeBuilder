from django.contrib.localflavor.us.models import USStateField
from django.db import models
from djang.db import datetime

# Create your models here.
class personal_Info(models.model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    e_add = models.CharField(max_length=50)
    Home_add = models.IntegerField.CharField(max_length=30)
    cell = models.CharField(max_length=10)
    links = models.CharField(max_length = 10**10)

    def __unicode__(self):
        return self.f_name

class Education_Background(models.model):
    gpa = models.FloatField(max_length=4)
    school_name = models.CharField(max_length=50)
    school_location = models.IntegerField.CharField(max_lenght=100)
    school_state = models.CharField(max_length=50)
    degree = models.charField(max_length=50)
    major = models.CharField(max_length=50)
    start_date = models.DateField(max_length=50)
    end_date = models.DateFeild(max_length=50)
    gradution_date = models.DateField(max_lenght=8)


class Work_Experience(models.model):
    employer = models.CharField(max_lenght=20)
    city = models.CharField(max_length=10)
    state = models.CharField(max_lenght=10)
    job_title = models.CharField(max_length=10)
    start_date = models.CharField(max_lenght=10)
    end_date = models.DateField(max_lenght=8)
    job_Responsabilities = models.CharField(max_length=10)

class skills(models.model):
    school = models.CharField(max_lenght=10)
    city = models.CharField(max_lenght=10)
    state = models.CharField(max_lenght=10)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=10)
    graduation_date = models.DateField(max_length=10)

class your_Project(models.model):
    N_proj = models.CharField(max_length=100**100)
    
class Award(models.model):
    award_name = models.CharField(max_length=50)
    award_date = models.DateField(max_length=10)
    awarder = models.CharField(max_lenght=10)
    Summary = models.CharField(max_length=10)
    