# bugtracker_app/urls.py
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name="signup"),
    path('createticket/', views.createticket, name="createticket"),
    path('ticketinfo/<int:ticketid>/', views.ticketinfo, name="ticketinfo"),
    path('filerinfo/<int:filerid>/', views.userinfo),
    path('ticketassignment/<int:ticketid>/inprogress/<int:userid>/',
         views.assignticket),
    path('ticketcomplete/<int:ticketid>/complete/<int:userid>/',
         views.completedticket),
    path('ticketinvalid/<int:ticketid>/invalid/<int:userid>/',
         views.invalidticket),
    path('ticketedit/<int:ticketid>/edit/', views.editticket)
]
