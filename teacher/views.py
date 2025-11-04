from django.shortcuts import render, redirect
from .models import Assignment
from student.models import Submission
from user.models import User
from .forms import AssignmentForm
from django.contrib import messages
from datetime import date

# Create your views here.

def teacher_dashboard(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user:login")
    
    teacher = User.objects.get(id=user_id)
    teacher_assignments = Assignment.objects.filter(teacher=teacher, teacher__course_class=teacher.course_class)

    pending_grading = Submission.objects.filter(student__role="student", student__course_class=teacher.course_class, graded=False)
    students = User.objects.filter(role="student", course_class=teacher.course_class)

    total_assignments = teacher_assignments.count()
    total_pending_grading = pending_grading.count()
    total_students = students.count()

    recent_assignments = teacher_assignments.order_by("-created_at")[:5]

    for assignment in recent_assignments:
        print(assignment.title, assignment.submissions.count())

    context = {
        "teacher": teacher,
        "total_assignments": total_assignments,
        "total_pending_grading": total_pending_grading,
        "total_students": total_students,
        "recent_assignments": recent_assignments,
        "today": date.today(),
    }
    return render(request, "teacher/teacher_dashboard.html", context)



def upload_assignment(request):

    teacher_id = request.session.get("user_id")
    teacher = User.objects.get(id=teacher_id)
    
    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            teacher_id = request.session.get("user_id")

            if not teacher_id:
                messages.error(request, "You must be logged in as a teacher!")
                return redirect("user:login_view")
            
            teacher = User.objects.get(id=teacher_id)
            assignment.teacher = teacher
            file = form.cleaned_data.get("file")
            due_date = form.cleaned_data.get("due_date")

            if due_date < date.today():
                messages.error(request, "Due date cannot be in the past!")
                return render(request, "teacher/upload_assignment.html", {"form":form})
            
            if file:
                if file.size > 10 * 1024 * 1024:
                    messages.error(request, "File size cannot be more than 10MB!")
                    return render(request, "teacher/upload_assignment.html", {"form":form})
                if not file.name.lower().endswith(".pdf"):
                    messages.error(request, "Only PDF files are allowed!")
                    return render(request, "teacher/upload_assignment.html", {"form":form})
                
            assignment.save()
            messages.success(request, "Assignment created successfully!")
            return redirect("teacher:teacher_dashboard")
        else:
            messages.error(request, "Invalid form submission!")
            return redirect("teacher:upload_assignment")
    else:
        form = AssignmentForm()

    return render(request, "teacher/upload_assignment.html", {"form":form, "teacher":teacher})



def grade_submissions(request):

    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user:login")

    teacher = User.objects.get(id=user_id)

    submissions = Submission.objects.filter(student__role="student", student__course_class=teacher.course_class, graded=False)

    if request.method == "POST":
        updated = False
        for submission in submissions:
            submission_id = submission.id
            grade = request.POST.get(f"grade_{submission_id}")
            remark = request.POST.get(f"remark_{submission_id}")

            if grade or remark:
                submission.grade = grade
                submission.remark = remark
                submission.graded = True
                submission.save()
                updated = True

        if updated:
            messages.success(request, "All results have been published successfully!")
        else:
            messages.info(request, "No grades or remarks entered.")
        
        return redirect("teacher:view_submissions")


    context = {
    "teacher": teacher,
    "submissions": submissions,
    }

    return render(request, "teacher/submission_page.html", context)


def view_submissions(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user:login")

    teacher = User.objects.get(id=user_id)

    assignments = Assignment.objects.filter(teacher=teacher)

    selected_assignment_id = request.GET.get("assignment_id")

    submissions = Submission.objects.filter(student__role="student", student__course_class=teacher.course_class, graded=True)

    if selected_assignment_id:
        submissions = submissions.filter(assignment_id=selected_assignment_id)

    context = {
    "teacher": teacher,
    "submissions": submissions,
    "assignments": assignments,
    "selected_assignment_id": selected_assignment_id
    }

    return render(request, "teacher/published_results.html", context)


def logout(request):
    request.session.clear()
    return redirect("user:login_view")
