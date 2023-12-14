# Homework-7

Install Python

    1. https://www.python.org/downloads/
    2. Download latest version and install.
    3. DO NOT forget to check the box for "Add Python to PATH". 

Clone the repository. 
```bash
#Clone
git clone https://github.com/ITEC660/homework-7-profkemalaydin #use your repository
cd homework-7-profkemalaydin #your folder
```

Virtual environment
```
#Install virtual environment
pip install virtualenv

#Create virtual environment
virtualenv env #you can name it anything, we use env

#Activate virtual environment 
#windows
cd env/Scripts
activate
cd ../.. #go to home folder

#mac
source env/bin/activate

#You will see (env) in the prompt which means your virtual environment is activated
```

Django
```
#install Django
pip install django

#check what is installed
pip freeze

#You should see something similar to
#asgiref==3.3.1
#Django==3.1.7
#sqlparse==0.4.3
#tzdata==2023.2
```

Create a project called **myproject** with the following steps:

```bash
#Start your project
django-admin startproject myproject
```

A directory called **myproject** should be created containing the default Django project structure with the following:

    manage.py
    myproject
        - __init__.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    

Now run the following commands 

```bash
#Enter your project directory
cd myproject

#run the project
python manage.py runserver
```

Go to *http://localhost:8000/* or *http://127.0.0.1:8000/* and make sure the installation works successfully.
You should see the template page. 

Create your app
```bash
django-admin startapp mycontactsapp
```
A directory called 'mycontactsapp' should be created containing the following structure:
```
    - admin.py
    - apps.py
    - migrations (folder)
    - models.py
    - tests.py
    - views.py
    - __init__.py    
```


**Let's create our first view**

Open the file mycontactsapp/views.py and edit:

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World')
```

Open the file myproject/myproject/urls.py and edit:

```python
from django.contrib import admin
from django.urls import path
from mycontactsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index')
]
```
Run server again
Go to [http://localhost:8000/](http://localhost:8000/) in your browser, and you should see the text: “Hello, world”, which you defined in the index view. Done!

**Create a Model**

Open the file mycontactsapp/models.py and edit:

```python
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
```

Open the file myproject/myproject/settings.py and add  the **'mycontactsapp'**  in INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mycontactsapp',
]
```

*Now run the command below to update the database*
```
python manage.py makemigrations mycontactsapp
```
You should see your version number in your terminal, something like:

    mycontactsapp/migrations/0001_initial.py

Make the following updates:

```bash
# Run your migration
python manage.py migrate

# Check if everything is passed, stated by an **… OK** ending

# create super user
python manage.py createsuperuser

# If you see the error below: 
# Superuser creation skipped due to not running in a TTY.
# You can try winpty
winpty python manage.py createsuperuser

# Serve the app
python manage.py runserver

```

Open the admin site [http://localhost:8000/admin/](http://localhost:8000/admin/)
You should be able to login and add users and groups.

**To see your models:**

```python
# Go to mycontactsapp open **admin.py** add the following code:

# Register your models here.
from .models import Contact
admin.site.register(Contact)
```

1. Refresh your admin page and you should now see the **Contacts**.
2. Insert three new contacts here.
3. Then display them with the following steps:

```python
# Edit **mycontactsapp/views.py 
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
```

[http://localhost:8000/](http://localhost:8000/) should display all your contacts with the format requested above.

Push all your updates to GitHub repository.

Add screenshots to your document in Canvas.
