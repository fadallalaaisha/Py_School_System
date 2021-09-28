import django
from student .models import Student
from django.shortcuts import render
from .models import Student
from .forms import StudentRegistrationForm
from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# that's where all the logics is 
def register_student(request):
    if request.method == 'POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:
        form=StudentRegistrationForm
    return render(request, 'register_student.html', {"form":form})
#Acceptes the requests
def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})

# Helps the existing student to edite their data
def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
    else:
        form=StudentRegistrationForm(instance=student)
    return render(request,"edit_student.html",{"form":form})

# Profile
def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":student}) 

# remove
def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")

# test_student list 
# test student profile
# test edit student
# test for the course    

# CI/CD helps one to colabrite eg a grope of team working togather in one django project.



















# def student_profile(request, id):
#     student = Student.objects.get(id==id)
#     return render(request,"student_profile.html",{"student":student})

# def edit_student(request,id):
#     student=Student.objects.get(id=id)
#     if request.method== "POST":
#         form=StudentRegistrationForm(request.Post,instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect("student_profile", id=student.id)

#         else:
#             form=StudentRegistrationForm(instance=student)
#             return render(request,"edit_student",{"form":form})


