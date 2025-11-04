from .models import Assignment
from django.forms import ModelForm
from django import forms

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        exclude = ["teacher", "created_at"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "placeholder": "e.g, Chapter 5 Exercises",
                "required": "true",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Provide detailed instructions..."
            }),
            "due_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "file": forms.ClearableFileInput(attrs={
                "class": "file-input",
                "id": "assignmentFile",
                "accept": ".pdf"
            }),
        }
