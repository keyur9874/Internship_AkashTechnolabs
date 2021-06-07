from django import forms
class Student(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.CharField()
    mobile_no = forms.IntegerField()
    local_address = forms.CharField()
    permanent_address = forms.CharField()
    pin_code = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput) 