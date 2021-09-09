from course .models import Course
from django.shortcuts import render, redirect
from .form import CourseForm
from.models import Course 

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

def course_list(request):
    courses=Course.objects.all()

    return render(request,"courses.html",{"courses":courses})
 
#  Editing
def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
    else:
        form=CourseForm(instance=course)
    return render(request,"edit_course.html",{"form":form})

# remove
def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect("course_list")
