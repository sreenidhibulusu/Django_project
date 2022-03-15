from django.shortcuts import render,redirect
from Myapp.models import Student

from django.http import HttpResponse
# Create your views here.

def nen(request):
    return HttpResponse('<h1><i style="color: pink;" >Helooooooo</i><h1>')

def name(request,name):
    return HttpResponse('<i>my name is {}</i>'.format(name))

def number(request,num):
    p = 0
    for i in range(num):
        p +=i
    return HttpResponse('the sum till now is {}'.format(p))


def table(request):
    return render(request,'Myapp/table.html')

def inline(request):
    return render(request,'Myapp/inline.html')

def external(request):
    return render(request,'Myapp/external.html')

def boot(request):
    return render(request,'Myapp/boot.html')
def offlinebt(request):
    return render(request,'Myapp/offlinebt.html')

def form(request):
    if request.method =='post':
        na = request.post['name']
        num = request.post['rollnum']
        age = request.post['age']
        mob = request.post['mobile']
        em = request.post['email']
        addr = request.post['address']
        Student.objects.create(name=na,rollnum=num,age=age,mobile=mob,email=em,address = addr)
        return redirect('/details')
    return render(request,'Myapp/form.html')

def details(request):
    data = Student.objects.all()
    return render(request,'Myapp/details.html',{'data':data})

def update(request,id):
    data = Student.objects.get(id=id)
    if request.method =='post':
        data.name = request.post['na']
        data.rollnum = request.post['num']
        data.age = request.post['age']
        data.mobile = request.post['mob']
        data.email = request.post['em']
        data.address = request.post['addr']
        data.save()
        
        return redirect('/details')
    return render(request,'Myapp/details.html',{'data':data})

def delete(request,id):
    ob= Student.objects.get(id=id)
    if request.method == "POST":
        ob.delete()
        return redirect('/details')
    return render(request,'Myapp/delete.html',{'info':ob})
    