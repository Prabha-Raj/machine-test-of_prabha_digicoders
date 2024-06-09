from django.shortcuts import render
from django.contrib import messages
from . models import Student
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        dob=request.POST['dob']
        category=request.POST['category']
        mobileno=request.POST['mobileno']
        password=request.POST['password']
        branch=request.POST['branch']
        collegename=request.POST['collegename']
        year=request.POST['year']
        emailaddress=request.POST['emailaddress']
        stu=Student(name=name,dob=dob, category=category, mobileno=mobileno, password=password, branch=branch, collegename=collegename, year=year,emailaddress=emailaddress)
        stu.save()
        messages.success(request, 'Student Registration is done')

    return render(request,"index.html",locals())
