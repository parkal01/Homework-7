from django.shortcuts import render

# Create your views here.
# import Contact from Models
from django.http import HttpResponse
from .models import Contact

def index(request):
    #return HttpResponse('Hello World')
    # Display contacts
    mylist = ""
    for i in Contact.objects.all():
        mylist += i.first_name + ', ' #update this code to list first name and last name as below
        # Henry Fox
        # James Brown
        # Kate Charnes
        # Make sure the list is alphabetically sorted.
    return HttpResponse("All Contacts:<br>" + mylist) 
    # update return: Center the list, 
    # and make two other css modifications as you wish.