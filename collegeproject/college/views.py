
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Departments, Courses,Purposes,Materials,Order
from datetime import date
# Create your views here.
# def index(request):
# #   obj1=Team.objects.all()
#     return render(request,"index.html")
def allDepartments(request):
      departs=Departments.objects.all()
      return render(request,"index.html",{'departs':departs})

def placeorder(request):
    # departs = Departments.objects.all()
    # return render(request,'placeorder.html',{'departs':departs})
    if request.method == 'POST':
        name=request.POST.get('name')

        dob = request.POST.get('dob')

        age = request.POST.get('age')

        #gender = str(request.POST["gender"].value)
        gender = request.POST.get('gender')
        if(gender=='option1'):
            gender="Female"
        else:
            gender="Male"

        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')

        department = request.POST.get("department")

        print('depart:',  department)
        course = request.POST.get('course')
        print('course:', course)
        purpose = request.POST.get('purpose')
        print('purpose:', purpose)
        materials=request.POST.getlist('checks[]')

        data = Order.objects.create(name=name, dob=dob,age=age,gender=gender,mobile=mobile,email=email,address=address,department=department,course=course,purpose=purpose,materials=materials)

        data.save()
        return redirect('/')
    departs = Departments.objects.all()
    purpose = Purposes.objects.all()
    materials=Materials.objects.all()
    return render(request,'order.html',locals())

def get_courses(request,department_name):
    department=Departments.objects.get(name=department_name)
    course=list(department.course.all().values())
    return JsonResponse(course,safe=False)


