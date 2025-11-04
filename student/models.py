from django.db import models
from user.models import User
from teacher.models import Assignment

# Create your models here.

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    file = models.FileField(upload_to='submissions/', null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)
    grade = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-submission_date']

    def __str__(self):
        return f"{self.student.full_name} → {self.assignment.title}"
