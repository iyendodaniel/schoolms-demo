from . import views
from django.urls import path
app_name = "student"

urlpatterns = [
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("submit/<int:assignment_id>/", views.submit_assignment, name="submit_assignment"),
    path("result/", views.result_view, name="results"),
    path("logout/", views.logout, name="logout"),    
]