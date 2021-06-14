from django.shortcuts import render, HttpResponseRedirect
from .forms import Student
from .models import User
from django.contrib import messages
# Create your views here.

# This Function For Add Student Data In Database


def add_show(request):

    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = Student()
    else:
        fm = Student()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# This Function for Delete Student Data From Database


def delete_data(request, s_id):
    if request.method == 'POST':
        s = User.objects.get(pk=s_id)
        s.delete()
        return HttpResponseRedirect('/')

# This Function  For Update Student Data


def update_data(request, s_id):
    if request.method == 'POST':
        pi = User.objects.get(pk=s_id)
        fm = Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Update Successfully")
        
    else:
        pi = User.objects.get(pk=s_id)
        fm = Student(instance=pi)
    return render(request, 'enroll/update.html', {'form': fm})
