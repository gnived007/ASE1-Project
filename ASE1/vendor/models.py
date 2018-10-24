from django.db import models


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=150)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    prod = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=150)
    qty = models.IntegerField(default=0)
    brand = models.CharField(max_length=150)
    photo = models.FileField(blank=True)

    def __str__(self):
        return self.prod_name
