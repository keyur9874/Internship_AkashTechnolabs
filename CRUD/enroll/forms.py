from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User

class Student(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {'name':forms.TextInput(attrs={"class":"form-control"}),
                    'email':forms.TextInput(attrs={"class":"form-control"}),
                    'password':forms.PasswordInput(render_value=True, attrs={"class":"form-control"}),
        }