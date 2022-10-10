from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	profile_img=models.ImageField(null=True,upload_to='profiles/',blank=True,default="profiles/default.png")
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	Date_of_Birth = models.DateField(null=True)
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

class Restaurant(models.Model):
	CATEGORY = (
			('Ethnics', 'Ethnics'),
			('Fast Food', 'Fast Food'),
			('Fast Casual', 'Fast Casual'),
			('Casual Dining', 'Casual Dining'),
			('Premium Casual', 'Premium Casual'),
			('family Style', 'family Style'),
			('Fine Dining', 'Fine Dining'),
			('Cafeteria', 'Cafeteria'),
			('Coffer House', 'Coffer House'),
			) 
	CUISIN = (
			('Bangladeshi','Bangladeshi'),
			('Chinses','Chinses'),
			('Indian','Indian'),
			('Pakistani','Pakistani'),
			('Thai','Thai'),
			('Arabian','Arabian'),

			)
	name = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	cuisin = models.CharField(max_length=200, null=True, choices=CUISIN)
	description = models.CharField(max_length=300, null=True, blank=True)
	# date_created = models.DateTimeField(auto_now_add=True, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

