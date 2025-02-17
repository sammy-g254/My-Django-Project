from django.http import HttpResponse
from django.template import loader

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