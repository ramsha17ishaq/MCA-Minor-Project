from django.shortcuts import render,HttpResponse
from .models import Appointment, Contact, FeedBack, Health_Campaign, Job, Test_Detail
from django.contrib import messages

# Create your views here

def home(request):
    # return(HttpResponse("<h1 style='color:green'> This is Home </h2>"))
    test_objects=Test_Detail.objects.all()
    health_objects=Health_Campaign.objects.all()
    job_object=Job.objects.all() #IT RETURNS QUERYSETS

    

    test_dict={
        "test_key": test_objects,
        "health_data":health_objects,
        "job_data":job_object
    }
    
    return render(request,'diagnosticcenter/html/dc_home.html',test_dict)

def job(request):
    job_object=Job.objects.all() #IT RETURNS QUERYSETS

    job_dict={"job_data":job_object}
    return render(request,'diagnosticcenter/html/dc_home.html',job_dict)

def campaign(request):
    health_objects=Health_Campaign.objects.all()
    health_dict={"health_data":health_objects}
    
    return render(request,'diagnosticcenter/html/dc_home.html',health_dict)

    # if request.method=="POST":
    #     return render(request,'diagnosticcenter/html/dc_home.html')

    # return render(request,'diagnosticcenter/html/dc_home.html')

def appointment(request):
    if request.method=="GET":
        test_objects=Test_Detail.objects.all()
        test_dict={
            "test_key": test_objects
        }
        return render(request,'diagnosticcenter/html/dc_home.html',test_dict)
    if request.method=="POST":
        user_name=request.POST["txtname"]
        user_phone=request.POST["txtphone"]
        user_email=request.POST["txtemail"]
        user_testname=request.POST["cmbtestname"]
        user_bookingtype=request.POST["bookingtype"]
       
        p=Appointment(Name=user_name,Phone=user_phone,Email=user_email,Test_name=user_testname,Booking_Type=user_bookingtype)
        p.save()
        messages.success(request,"Thank You .. You will get an confirmation email in 30 minutes")
        return render(request,'diagnosticcenter/html/dc_home.html')


    


def contactus(request):
    
    if request.method == "GET":
        return render(request,'diagnosticcenter/html/contactus.html')

    if request.method == "POST":
        user_name=request.POST["txtname"]  #request.POST is dictionary and control names are keys here
        # request.POST.get("txtname")
        user_email=request.POST["txtemail"]
        user_phone=request.POST["txtphone"]
        user_query=request.POST["txtquery"]

        c=Contact(Name=user_name,Email=user_email,Phone=user_phone,Your_query=user_query) #OBJECT CREATION
        c.save() #ORM concept= object saving and it will store data into Contact table using ORM
        print("Contact saved successfully")
        messages.success(request,"Thank You for contacting us , we will reach you soon  ")

        return render(request,'diagnosticcenter/html/contactus.html')


def feedback(request):
    
    if request.method == "GET":
        return render(request,'diagnosticcenter/html/feedback.html')

    if request.method == "POST":
        user_name=request.POST["txtname"]
        user_email=request.POST["txtemail"]
        user_feedback=request.POST["txtfeedback"]
        user_ratings=request.POST["txtratings"]

        f=FeedBack(Name=user_name,Email=user_email,Feedbacktext=user_feedback,Rating=user_ratings,)
        f.save()
        print("Feedback saved successfully")
        messages.success(request,"Thank You for your feedback, we will try to give our best" )
        return render(request,'diagnosticcenter/html/feedback.html')

def services(request):
    return render(request, 'diagnosticcenter/html/services.html')


def aboutus(request):
    return render(request,'diagnosticcenter/html/aboutus.html')


def pathologist(request):
    return render(request, 'diagnosticcenter/html/pathologist.html')

def radiologist(request):
    return render(request, 'diagnosticcenter/html/radiologist.html')
    
def cardiologist(request):
    return render(request, 'diagnosticcenter/html/cardiologist.html')

def neurologist(request):
    return render(request, 'diagnosticcenter/html/neurologist.html')


def emergency(request):
    return render(request, 'diagnosticcenter/html/emergency.html')
