from django.db import models
from user.models import User
# Create your models here.

# ========= Assignment ===========

class Assignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    file = models.FileField(upload_to="assignment/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title