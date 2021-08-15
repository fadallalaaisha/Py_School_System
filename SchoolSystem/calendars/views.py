#from SchoolSystem.course.form import CourseForm
from calendars .models import Calendar
from django.shortcuts import render
from .form import CalendarForm  


def register_Calendar(request):
    if request.method == 'POST':
        form=CalendarForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    

    else:
            form=CalendarForm()

    return render(request,'calendar.html',{"form":form})
    
