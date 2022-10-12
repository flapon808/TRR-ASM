from django.db import models
from datetime import datetime



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Cuisin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Price(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name



class Product(models.Model):
    image = models.ImageField(upload_to="dish/")
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    cuisin = models.ForeignKey(Cuisin, on_delete=models.CASCADE, default=False, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, default=False, null=True)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)
