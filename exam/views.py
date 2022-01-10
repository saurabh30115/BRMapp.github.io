from django.shortcuts import render
from django.http import HttpResponse
def showTest(request):
    que="who devoplop c language"
    a="ken thomsan"
    b="Dennis Ritchie"
    c="Bjarne Stroustrup"
    d="James Gosling"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(request):
    s="<h1>show result</h1>"
    return HttpResponse(s)
