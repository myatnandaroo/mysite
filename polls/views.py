from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Student
from django.urls import reverse

# def index(request):
#     return HttpResponse("Hello world!")


def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())



def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# def index(request):
#     stu = Student.objects.all().values()
#     output = ""
#     for x in stu:
#         output += x["firstname"]
#         return HttpResponse(output)

def name(request):
    stu = Student.objects.all().values()
    template = loader.get_template('name.html')
    context = {'mystu': stu,}
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  stu = Student(firstname=x, lastname=y)
  stu.save()
  return HttpResponseRedirect(reverse('index'))