from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=150)

    def __str__(self):
        return self.cat_name


# class SubCategory(models.Model):
#     sub_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
#     sub_cat_name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.sub_cat_name
#

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=150)
    #prod_description = models.TextField(max_length=150)
    qty = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    brand = models.CharField(max_length=150, blank=True)
    photo = models.FileField(blank=True)

    def __str__(self):
        return self.prod_name


class VendorProfile(models.Model):
    Vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True)