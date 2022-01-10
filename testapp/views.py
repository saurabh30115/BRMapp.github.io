
from django.http import HttpResponse
from django.shortcuts import render
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
def greeting(request):
     s="<h1>hello and welcome to the first view of testapp</h1><p>this is landing page</p>"
     return HttpResponse(s)
def showContact(request):
    s="<h1>contact page</h1>"
    s+="<p>website: mysirg.com</p>"
    s+="<p>mobile: 8225953075</p>"
    s+="<p>Email:saurabh802221@gmail.com</p>"
    return HttpResponse(s)
def about(request):
    return render(request,'testapp/about.html')
