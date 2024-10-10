from django.db import models 
# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField(default=24)
    notes = models.CharField(max_length=100)
    phone = models.IntegerField(default=1234567890)


    def __str__(self):
        return f"name --> {self.name}"