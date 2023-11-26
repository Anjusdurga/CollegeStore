from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from college.models import Departments
from datetime import date

# def calculate_age(born):
#     today = date.today()
#     try:
#         birthday = born.replace(year=today.year)
#     except ValueError: # raised when birth date is February 29 and the current year is not a leap year
#         birthday = born.replace(year=today.year, month=born.month+1, day=1)
#     if birthday > today:
#         return today.year - born.year - 1
#     else:
#         return today.year - born.year

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':

        username=request.POST.get('username')
        firstname = request.POST.get('firstname')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        value = {
            "username": username,
            "firstname": firstname,
             }

        error_message=None

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                    error_message='User name already exist..'

        else:
            error_message="Passwords not matched"


        if not error_message:
            user = User.objects.create_user(username=username, first_name=firstname,
                                            password=password)
            user.save()
            return redirect('/credentials/login')
        else:
            data={
                'error' :error_message,
                'values':value
            }
            return render(request, 'register.html',data)
    return render(request,'register.html')

