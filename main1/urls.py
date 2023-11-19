#from django.contrib import admin
from django.urls import path
from main1.views import Home, About, service, contact_us

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('service/', service.as_view(), name='service'),
    path('contact_us/', contact_us.as_view(), name='contact_us')
]
