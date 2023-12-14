from django.contrib import admin

# Register your models here.
# Go to mycontactsapp open **admin.py** add the following code:

# Register your models here.
from .models import Contact
admin.site.register(Contact)