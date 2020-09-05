# bugtracker
Django bug tracking support system

Author: Ally Engle

Assessment: Bug Tracker

Academic Integrity Reminder: To give proper citation, this is taken from "Avoiding Plagiarism: Academic Integrity @ Butler <https://libguides.butler.edu/c.php?g=34302&p=218280>", should you want to give the full article a read. It's on Butler's Academic Integrity Policy, which Kenzie is partnered with.


    Cheating includes receiving or giving help on papers, experiments, reports, compositions, projects or examinations without the instructor's permission. It also includes submitting part of or all of the completed assignment of another student as one's own work. Of special note and concern is the use of purchased research papers. It is a violation of the regulations of Butler University for a student to purchase a term paper. Cheating is also using unauthorized materials and aids, such as books, one's own notes or those of another and calculators during an examination.

    Plagiarism is the fraudulent misrepresentation of any part of another person's work as one's own. Submitting any writing, including take-home exams, that does not properly acknowledge the quoting or paraphrasing of another person's words, or that fails to give proper credit for another person's ideas, opinion, or theory is plagiarism. Any unacknowledged use of sources to which one is indebted including but not limited to, music, video, audio, theatre projects, compositions, website and computer software constitutes plagiarism.
    
(I already cite heavily to comply with the cheating and plagiarism sections. However, this specfic assessment just took from 8/26-9/4 to get done, not because I was plagiarising but because of Academic interference issues that were preventing me from getting my assesment done. Also, on the continued issue with cloning, it wasn't a problem from about 8/24 until 9/2 and then it started to kick up again when I released the first part of bugtracker, which is literally just the whole of custom user model, which also suddenly has the cloning issue again that didn't exist from 8/26-9/2 which I used a tutorial for to get through, so I'm curious why it's suddenly an issue again, after a week of it not being an issue, and why both have 14+ unique clones and 14+ clones on both, when there should only be 2 unique cloners and 2 clones on this?? Please see the following 2 paragraphs regarding facilitation of Academic Dishonesty and Academic Interference since the cloning issue continues to be an issue and a case could be made for it being facilitation of Academic Dishonesty and Academic Interference, non-Kenzie perssonal factors in my case included and considered.)
    
    Facilitating Academic Dishonesty involves assisting someone in an act of dishonesty.

    Interference includes the theft, alteration, destruction or obstruction of another student's work. Interference may take the form of the theft, defacements       or destruction of resources, e.g., library periodicals and books, so as to deprive other students of information.

Coding Plan: (So far)

    1. Custom User Model/Authentication-completed
    2. Bug tracker-completed 9/4/2020


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



