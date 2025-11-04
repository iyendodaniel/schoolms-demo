from . import views
from django.urls import path
app_name = "teacher"

urlpatterns = [
    path("teacher-dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("upload/", views.upload_assignment, name="upload_assignment"),
    path("grade/", views.grade_submissions, name="grade_submissions"),
    path("submissions/", views.view_submissions, name="view_submissions"),
    path("logout/", views.logout, name="logout"),
]