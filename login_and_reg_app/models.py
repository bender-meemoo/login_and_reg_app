from django.db import models
import bcrypt
import re

# Create your models here.

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) == 0:
            errors['fname'] = "First name is required!"
        elif len(postData['fname']) < 2:
            errors['fname'] = 'First name should at leat be 2 characters.'
        
        if len(postData['lname']) == 0:
            errors['lname'] = "FLast name is required!"
        elif len(postData['lname']) < 2:
            errors['lname'] = 'Last name should at leat be 2 characters.'

        if len(postData['useremail']) == 0:
            errors['useremail'] = "Email is required!"    
        elif not EMAIL_REGEX.match(postData['useremail']):          
            errors['useremail'] = "Invalid email address!"
        
        if len(postData['pwd']) == 0:
            errors['pwd'] = 'Password is required'
        elif len(postData['pwd']) < 8:
            errors['pwd'] = 'Password must be 8 characters.'
        
        if  postData['pwd'] != postData['confirmpwd']:
            errors['confirmpwd'] = 'Password must match'

        return errors
    def loginValidator(self, postData):
        errors = {}
        emailMatch = user.objects.filter(email = postData['useremail'])
        print("^^^^^^^^^^^^^^^^^^^^^^", emailMatch[0].password)
        if len(emailMatch) == 0:
            errors['useremail'] = 'Email not found'
        elif not bcrypt.checkpw(postData['pwd'].encode(), emailMatch[0].password.encode()):
            errors['loginpw'] = 'Incorrect password.'
        # elif emailMatch[0].password != postData['pwd']:
        #     errors['loginpw'] = 'Incorrect password.'
        # bcrypt.checkpw('test'.encode(), hash1.encode())
        return errors

class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    objects = userManager()