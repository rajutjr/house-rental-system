from django.db import models

# Create your models here.
from email.policy import default
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class MILL(models.Model):
    OWNER_NAME=models.CharField(max_length=100)
    COST=models.IntegerField(default=100)
    UPLOAD_IMAGE1=models.ImageField(upload_to='new pics',default="NULL")
    UPLOAD_IMAGE2=models.ImageField(upload_to='new pics',default="NULL")
    UPLOAD_IMAGE3=models.ImageField(upload_to='new pics',default="NULL")
    ADDRESS=models.TextField(default="vignan")
    
    ENTER_LOCATION=models.URLField(max_length=2000,default='NULL')
    
    
    STATE=models.CharField(max_length=50,default="krishna", choices= [             
            ('vizag', 'vizag'), 
            ('krishna', 'krishna'), 
            ('nellore', 'nellore'),  
            ('east godavari','east godavari'),
            ('chittor','chittor'),
            ('guntur','guntur'),  
            ('srikakulam','srikakulam'),
            ('kakinada','kakinada'),    
        ])
    CHOOSE_TYPE=models.CharField(max_length=50,default="cold storage",choices=[
        ('market','market'),
        ('cold storage','cold storage'),

    ])    

    VIDEO=models.FileField(upload_to='videos/',default="NULL")
    def __str__(self):
        return self.OWNER_NAME

  
  

# admin created houses

class adminhouses(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")
class adminhouses2(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")

class adminhouses3(models.Model):
    IMAGE=models.ImageField(upload_to="pics",default="NULL")
    PRICE=models.IntegerField(default=250)
    PLACE=models.TextField(default="VIZAG")






class house(models.Model):
    type=models.CharField(max_length=200)
    cost=models.IntegerField(default=15)
    img=models.ImageField(upload_to='pics quaality')
    facility=models.TextField(default="3BHK") 
    phone=models.IntegerField(default=15)   
    

class dest1(models.Model):
    type=models.CharField(max_length=200)
    cost=models.IntegerField(default=15)
    img=models.ImageField(upload_to='pics quaality')
    facility=models.TextField(default="3BHK") 
    phone=models.IntegerField(default=15)   
class excel(models.Model):   
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    graduation=models.CharField(max_length=100)
    technologies=models.TextField() 
class hello(models.Model):   
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    graduation=models.CharField(max_length=100)
    technologies=models.TextField() 
    resume=models.TextField(default="NULL")    



# new fields and fields options
class officer(models.Model):
    name=models.CharField(max_length=100,verbose_name="hello fill it",blank=True,null=True)
    second_name=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)

    gender_choices=[


        ('m',"male"),
        ('f',"female"),
        ('o',"others"),
    ]
    gender=models.CharField(max_length=20,choices=gender_choices,default="SUCCESS")