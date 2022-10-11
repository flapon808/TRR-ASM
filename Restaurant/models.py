from django.db import models
from datetime import datetime
# Create your models here.

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
class Comment(models.Model):
    product = models.ForeignKey(Restaurant, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)