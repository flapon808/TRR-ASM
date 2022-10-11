from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	profile_img=models.ImageField(null=True,upload_to='profiles/',blank=True,default="profiles/default.png")
	fullname = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_of_birth = models.DateField(null=True)
	GENDER=(
        	('Male','Male'),
        	('Female','Female'),
       		('Other','Other'),
	)
	gender = models.CharField(max_length=6, blank=True, null=True, choices= GENDER,)
	def __str__(self):
		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name



