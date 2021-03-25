from django.core.exceptions import ValidationError
from django.db import models
import bcrypt

class Validate(models.Manager):
    def validateLogin(self, form):
        errors={}
        check_user = User.objects.filter(email=form['email'])
        if not check_user:
            errors['email'] = 'Invalid email/password'
            return errors
        else:
            pwd = form['password']
            check_pwd = bcrypt.checkpw(pwd.encode(), check_user[0].password.encode())
            if not check_pwd:
                errors['password'] = 'Invalid email/password'
        return errors 

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validate()

class Credit_card(models.Model):
    cc_name = models.CharField(max_length=45)
    cc_url = models.CharField(max_length=150)
    cc_type = models.CharField(max_length=45)
    user = models.ManyToManyField(User, related_name="credit_card")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Program(models.Model):
    program_name = models.CharField(max_length=45)
    program_url = models.CharField(max_length=45)
    credit_card = models.ForeignKey(Credit_card, related_name="program", on_delete=models.PROTECT, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Retailer(models.Model):
    retail_name = models.CharField(max_length=45)
    retail_url = models.CharField(max_length=45)
    category = models.CharField(max_length=45, null=True)
    credit_card = models.ManyToManyField(Credit_card, through='Reward', related_name="retailer")
    user = models.ManyToManyField(User, related_name="retailer")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Reward(models.Model):
    credit_card = models.ForeignKey(Credit_card, related_name='rewards', on_delete=models.PROTECT, null=True)
    retailer = models.ForeignKey(Retailer, related_name='rewards', on_delete=models.PROTECT, null=True)
    points = models.IntegerField()
