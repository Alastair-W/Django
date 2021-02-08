from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

def validateLengthGreaterThanTen(value):
    if len(value) < 11:
        raise ValidationError(
            '{} must be longer than: 10'.format(value)
        )

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=100)