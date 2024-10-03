from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("",views.job,name="job"),
    path("",views.campaign,name="campaign"),
    path("contactus/",views.contactus,name="contactus"),
    path("feedback/",views.feedback,name="feedback"),
    path("services/",views.services,name="services"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("appointment/",views.appointment,name="appointment"),
    path("pathologist/",views.pathologist,name="pathologist"),
    path("radiologist/",views.radiologist,name="radiologist"),
    path("cardiologist/",views.cardiologist,name="cardiologist"),
    path("neurologist/",views.neurologist,name="neurologist"),
    path("emergency/",views.emergency,name="emergency"),



]