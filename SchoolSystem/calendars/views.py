# from calendars .models import Calendar
# from django.shortcuts import render
# from .form import CalendarForm  
# from.models import Calendar

# def register_Calendar(request):
#     if request.method == 'POST':
#         form=CalendarForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)    
#     else:
#         form=CalendarForm()
#     return render(request,'calendar.html',{"form":form})
    
# def calendar_list(request):
#     calendars=Calendar.objects.all()
#     return render(request,"calendar_list.html",{"calendar":calendars})

# from SchoolSystem import calendars
from django.shortcuts import render

def register_calendar(request,year,month):
    calendars="Aisha"
    return render(request,'calendar.html',{"name":calendars,"year":year,"month":month,})










# import sys
# sys.setrecursionlimit(10000)
# from datetime import date, datetime
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic
# from django.utils.safestring import mark_safe

# from .models import *
# from .utils import Calendar

# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'calendars/calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('day', None))

#         # Instantiate our calendar class with today's year and date
#         cal = Calendar(d.year, d.month)

#         # Call the formatmonth method, which returns our calendar as a table
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendars'] = mark_safe(html_cal)
#         return context

# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()    