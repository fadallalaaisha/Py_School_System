#from SchoolSystem.course.form import CourseForm
from course .models import Course
from django.shortcuts import render
from .form import CourseForm  


def register_Course(request):
    if request.method == 'POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    

    else:
            form=CourseForm()

    return render(request, 'courseTemplate.html', {"form":form})
    
