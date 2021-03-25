from django import forms
from .models import *


def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

def validateLengthGreaterThanTen(value):
    if len(value) < 11:
        raise ValidationError(
            'Your password must be longer than: 10'.format()
        )

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators = [validateLengthGreaterThanTen])
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)