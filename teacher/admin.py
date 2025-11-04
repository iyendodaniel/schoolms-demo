from django.contrib import admin
from .models import Assignment

# Register your models here.

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "title", "due_date", "file")