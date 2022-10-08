from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

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
			('Bangladeshi ','Bangladeshi '),
			('Chinses ','Chinses '),
			('Indian ','Indian '),
			('Pakistani ','Pakistani '),
			('Thai ','Thai '),

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




	
