from django.contrib import admin
from .models import Submission

# Register your models here.

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("student", "submission_date", "file")