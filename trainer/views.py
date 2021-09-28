# from SchoolSystem.student.forms import StudentRegistrationForm
from trainer .models import Trainer
from .forms import TrainerRegistrationForm
from .models import Trainer
from django.shortcuts import render,redirect
from django.http.response import HttpResponse 
from django.shortcuts import render
# import django

def register_trainer(request):
    if request.method == 'POST':
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:
         form=TrainerRegistrationForm()
    return render(request, 'register_trainer.html', {"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer.html",{"trainers":trainers})

# Editing part
# Helps the existing student to edite their data
def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainer)
    return render(request,"edit_trainer.html",{"form":form})

# Profile
def trainer_profile(request,id):
   trainer=Trainer.objects.get(id=id)
   return render(request,"trainer_profile.html",{"trainer":trainer}) 

# remove
def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("trainer_list")
 

