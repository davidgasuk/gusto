import os

from django.db import models
from uuid import uuid4
import os
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.category_order}'

class Dish(models.Model):
    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to=get_file_name_dishes)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)