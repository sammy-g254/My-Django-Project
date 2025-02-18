from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("hello world")
def index(request):
    return HttpResponse("About eMobilis")
def myfunction(request):
    return HttpResponse('Hello,from myfunction')
def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())
def contact(request):
    my_template_data={
        'title':'home',
        'name':'jane',
        'message':'this is the homepage',
        'year':2025
    }
    return render(request,'home.html',my_template_data)
def services(request):
    return render(request, 'services.html')
def contactus(request):
    return render(request, 'contactus.html')