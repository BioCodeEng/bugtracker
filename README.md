# bugtracker
Django bug tracking support system

Author: Ally Engle

Assessment: Bug Tracker

Coding Plan: (So far)

    1. Custom User Model/Authentication
    2. Bug tracker
        a. CRUD
        b. ticket_detail
        c. user_detail


    My apologies for not getting this done sooner, I've ran into tech issues beyond my control and have done this 3 or 4 times, I'm not even kidding.

Sources for assistance in understanding concepts: Sources will be referenced for example with [R1]

Previous Assesssments that taught concepts:

 [A1] Recipebox, especially authentication

 [A2] Custom User Model Assessment

    Will be using that as a component of this, especially the login, logout, signin and registration components

  Outside Sources used:

 [R1] Djangoproject.com (Various sections and subjections noted individually below)

    .1 Model field reference <https://docs.djangoproject.com/en/3.1/ref/models/fields/>
    .2 #choices <https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices>
    .3 Using the Django authentication system <https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-in>


 [R2] How to Use Django's Built-in Login System <https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html>

 [R3] Django: Display Choice Value <https://stackoverflow.com/questions/4320679/django-display-choice-value>

 [R4] Django CRUD (Create, Retrieve, Update, Delete) Function Based Views <https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/>

 [R5] Django CRUD Web Application <https://medium.com/@john.bagiliko/django-crud-web-application-77ef05af1f00>

 [R6] Working with Django Templates & Static Files <https://scotch.io/tutorials/working-with-django-templates-static-files>
        
      Tutorial over static files, templates, partials, base extension and navbar
      
      {% include 'partials/nav-bar.html' %}
      {% url 'data' %}



