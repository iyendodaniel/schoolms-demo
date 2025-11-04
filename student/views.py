from django.shortcuts import render, redirect
from .models import Assignment
from student.models import Submission
from user.models import User
from datetime import date
from django.contrib import messages
from .forms import SubmissionForm

# Create your views here.

def student_dashboard(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user:login")
    
    student = User.objects.get(id=user_id)

    class_assignments = Assignment.objects.filter(teacher__course_class=student.course_class)
    total_class_assignments = class_assignments.count()

    submitted_assignments = Submission.objects.filter(student=student).values_list("assignment_id", flat=True)
    total_submitted_assignments = submitted_assignments.count()

    pending_assignments = class_assignments.exclude(id__in=submitted_assignments)
    total_pending_assignments = pending_assignments.count()

    available_assignments = class_assignments[:5]

    context = {
        "student": student,
        "total_class_assignments": total_class_assignments,
        "total_submitted_assignments": total_submitted_assignments,
        "total_pending_assignments": total_pending_assignments,
        "available_assignments": available_assignments,
        "submitted_ids": submitted_assignments,
        "today": date.today(),
    }
    return render(request, "student/student_dashboard.html", context)


def submit_assignment(request, assignment_id):
    student_id = request.session.get("user_id")
    student = User.objects.get(id=student_id)

    assignment = Assignment.objects.get(id=assignment_id)

    existing_submission = Submission.objects.filter(student=student, assignment=assignment).first()
    if existing_submission:
        messages.warning(request, "You have already submitted this assignment!")
        return redirect("student:student_dashboard")

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)

        if form.is_valid():  
            submission = form.save(commit=False)

            submission.student = student
            submission.assignment = assignment
            submission.graded=False
            submission.submission_date = date.today()

            file = form.cleaned_data.get("file")

            if file:
                if file.size > 10 * 1024 * 1024:
                    messages.error(request, "File size cannot be more than 10MB!")
                    return render(request, "student/submission_assignment_page.html", {'form': form, 'assignment': assignment})
                if not file.name.lower().endswith(".pdf"):
                    messages.error(request, "Only PDF files are allowed!")
                    return render(request, "student/submission_page.html", {'form': form, 'assignment': assignment})
                
            submission.save()
            messages.success(request, "Assignment submitted successfully!")
            return redirect("student:student_dashboard")

        else:
            messages.error(request, "Invalid form submission!")
            return redirect("student:submit_assignment")
    else:
        form = SubmissionForm()
    return render(request, "student/submission_assignment_page.html", {'form': form, 'assignment': assignment})


def result_view(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user:login")
    
    student = User.objects.get(id=user_id)

    graded_submissions = Submission.objects.filter(student=student, graded=True, assignment__teacher__course_class=student.course_class).order_by("-submission_date")

    context = {
        "student": student,
        "graded_submissions": graded_submissions,
    }
    return render(request, "student/results.html", context)


def logout(request):
    request.session.clear()
    return redirect("user:login_view")
