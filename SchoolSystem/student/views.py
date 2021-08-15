from student .models import Student
from django.shortcuts import render
from.models import Student
from .forms import StudentRegistrationForm

from.models import Student


# Create your views here.
# that's where all the logics is done eg accepts requset and give feedbacks

# from.forms import StudentRegisterationForm

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

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":Student})

#Acceptes the requests
def student_list(request):
    students=Student.objects.all()

    return render(request,"student_list.html",{"students":students})

