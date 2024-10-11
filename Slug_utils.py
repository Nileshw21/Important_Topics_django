# utils.py

import django
import itertools
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()
from django.template.defaultfilters import slugify
import uuid


def generateSlug(name, ModelClass):
    new_slug = slugify(name)
    if ModelClass.objects.filter(slug = new_slug).exists():
        new_slug = f"{new_slug}-{str(uuid.uuid4()).split('-')[0]}"

    return new_slug




#######################################################################################################
# models.py

# from django.db import models
# from home.utils import generateSlug


# class Brand(models.Model):
#     brand_name = models.CharField(max_length=100)
#     country = models.CharField(default="IN",max_length=100)

#     def __str__(self):
#         return self.brand_name
    

# class Products(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True , blank = True)
#     product_name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, null=True , blank=True)

#     def save(self, *args, **kwargs) -> None:
#         if not self.id:
#             self.slug = generateSlug(self.product_name , Products)
#         return super().save(*args, **kwargs)
