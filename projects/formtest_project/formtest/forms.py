from django import forms
from .models import *

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators = [validateLengthGreaterThanTen])
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)