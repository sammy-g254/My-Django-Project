from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('myurl/',views.myfunction,name='myurl'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('services/',views.services,name="services"),
    path('contactus/',views.contact_us,name="contactus")
]