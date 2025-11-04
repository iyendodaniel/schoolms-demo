from django import forms
from .models import Submission
from django.forms import ModelForm

class SubmissionForm(ModelForm):
    class Meta():
        model = Submission
        fields = ["file"]
        widgets = {
            "file": forms.ClearableFileInput(attrs={
                "class": "file-input",
                "id": "assignmentFile",
                "accept": ".pdf"
            })
        }