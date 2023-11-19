#from django.shortcuts import render
from django.views.generic import ListView
from main1.models import Home, About, service, contact_us

class Home(ListView):
    model = Home
    template_name = 'layouts/index.html'



class About(ListView):
    model = About
    template_name = 'layouts/about.html'


class service(ListView):
    model = service
    template_name = 'layouts/service.html'


class contact_us(ListView):
    model = contact_us
    template_name = 'layouts/contact.html'

