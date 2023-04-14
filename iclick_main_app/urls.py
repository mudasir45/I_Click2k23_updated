from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('userSignUp/', views.userSignUp, name='userSignUp'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('userLogout/', views.userLogout, name='userLogout'),
    # path('stdlogin', views.stdlogin, name='stdlogin'),
    # path('revlogin', views.revlogin, name='revlogin'),
    # path('rev', views.admin1, name='rev'),
    # path('adminrev', views.adminrev, name='adminrev'),
    # path('student', views.student, name='student'),
    # path('submitrev', views.submitReviwe, name='submitReviwe'),
    # path('stdupdateprofile', views.stdupdate, name='stdupdate'),
    # path('stdupdatedone', views.stdupdatedone, name='stdupdatedone'),
    path('alert', views.alert, name='alert'),
    path('check_username_availability/', views.check_username_availability, name='check_username_availability'),

] 
