from django.shortcuts import render
from .forms import Student
# Create your views here.

def StudForm(request):
    fm = Student()
    return render(request,'application/forms_page.html',{'form':fm})