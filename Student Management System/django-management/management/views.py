from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q  # Import Q for complex queries


def student_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        students = Student.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
    else:
        students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students, 'query': query})

# Display the details of a single student
def student_detail(request, pk):
    print(f"Fetching details for student with pk: {pk}")
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'management/student_detail.html', {'student': student})

# Add a new student
@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student has been created successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'There was an error creating the student. Please correct the form below.')
    else:
        form = StudentForm()
    return render(request, 'management/student_form.html', {'form': form})

# Edit an existing student's information
@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student information has been updated successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'There was an error updating the student. Please correct the form below.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'management/student_form.html', {'form': form})

# Delete an existing student
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student has been deleted successfully!')
        return redirect('student_list')  # Redirect to the student list after deletion
    return render(request, 'management/student_detail.html', {'student': student})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! Please log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'There was an error creating your account. Please correct the form below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in!')
                return redirect('student_list')  # Redirect to student list after login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return redirect('forgot_password')

        # Validate the new password
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('forgot_password')

        # Here you can add more password validations as per your requirements
        if len(new_password) < 8:
            messages.error(request, 'New password must be at least 8 characters long.')
            return redirect('forgot_password')

        # Set the new password and save
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Your password has been successfully updated! Please log in with your new password.')
        return redirect('login')  # Redirect to the login page after successful password update
    return render(request, 'registration/forgot_password.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')  # Redirect to the login page after logout