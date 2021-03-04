from django.shortcuts import render, HttpResponse, redirect
from .models import user
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginuser(request):
    print(request.POST)
    print('**********************************')
    errors = user.objects.loginValidator(request.POST)
    print('************************ERRORS', errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    emailMatch = user.objects.filter(email = request.POST['useremail'])
    request.session['userID'] = emailMatch[0].id
    return redirect('/success')

def createuser(request):
    errors = user.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    hashpwd = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt()).decode()

    newuser = user.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['useremail'], password = hashpwd)
    request.session['userID'] = newuser.id
    return redirect('/success')

def success(request):
    if 'userID' not in request.session:
        messages.error(request, 'You must be logged in to use this page. Please register or log in.')
        return redirect('/')
    context = {
        "user": user.objects.get(id = request.session['userID'])
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')