from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm  # This form needs to be created

# Display a list of all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students})

# Display the details of a single student
def student_detail(request, pk):

    print(f"Fetching details for student with pk: {pk}")
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'management/student_detail.html', {'student': student})

# Add a new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'management/student_form.html', {'form': form})

# Edit an existing student's information
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'management/student_form.html', {'form': form})
