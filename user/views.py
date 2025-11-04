from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import User
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not found.")
            return redirect("user:login_view")
        if user.password != password:
            messages.error(request, "Incorrect password.")
            return redirect("user:login_view")
        request.session["user_id"] = user.id
        request.session["role"] = user.role
        request.session["full_name"] = user.full_name
        if user.role == 'student':
            return redirect('student:student_dashboard')
        if user.role == 'teacher':
            return redirect('teacher:teacher_dashboard')
    return render(request, 'user/login.html')



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get("password")
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect("user:signup")
            if len(full_name.split()) < 2:
                messages.error(request, "Please enter both first and last name!")
                return redirect("user:signup")
            if len(password) < 8:
                messages.error(request, "Password must have at least 8 characters!")
                return redirect("user:signup")
            
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("user:login_view")
        else:
            messages.error(request, "Invalid form submission!")
            return redirect("user:signup")
    else:
        form = UserForm()
        return render(request, 'user/signup.html')