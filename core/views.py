from django.shortcuts import render
from student.models import Student
from course.models import Course
from trainer.models import Trainer
from cal.models import Event


# Create your views here.
def home(request):
    students = Student.objects.count()
    courses = Course.objects.count()
    trainers = Trainer.objects.count()
    cals = Event.objects.count()

    data={"students":students,"courses":courses,"trainers":trainers,"cals":cals,}
    return render(request,"home.html",data)

   