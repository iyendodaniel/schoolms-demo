from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    course_class = models.CharField(max_length=50)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name