from django.contrib import admin
from .models import Test_Detail, Health_Campaign, Contact, FeedBack, Job, Appointment
# Register your models here.

class Admin_contact(admin.ModelAdmin):
    list_display = ('Your_query',)

class Admin_feedback(admin.ModelAdmin):
    list_display = ('Feedbacktext',)

class Admin_job(admin.ModelAdmin):
    list_display = ('PostName','NoOfseats',)


class Admin_appointment(admin.ModelAdmin):
    list_display = ('Booking_Type',)
    


admin.site.register(Test_Detail)
admin.site.register(Health_Campaign)
admin.site.register(Contact,Admin_contact)
admin.site.register(FeedBack,Admin_feedback)
admin.site.register(Job,Admin_job)
admin.site.register(Appointment,Admin_appointment)


admin.site.site_header = "Diagnostic Centre Administrations"
admin.site.site_title = "Diagnostic Admin Dashboard"
admin.site.index_title = "Welcome to Our Diagnostic Centre"

