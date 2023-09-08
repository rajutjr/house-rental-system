from django.urls import path
from . import views
urlpatterns=[
 path('',views.start,name='home'),#home page
 path("page1",views.page1,name='firstpage'),# first page after login
  path("uploaded",views.uploaded,name="uploaded"),#to see uploaded houses(explore) " second page"
 
 path("register",views.register,name="register"),#for user entering house details

 
 
 path("projectregister",views.projectregister,name="projectregister"),#user self details for registration  "" projectregister.html"
 path("login",views.login,name='login'),# for user login
path("next",views.details,name="details"),#for third page
path("excel",views.excelsheet,name="excel"),#for excel page
path("my_view/",views.my_view,name="my_view"),
path("logout",views.logoutUser,name="logout"),
path("ready/",views.ready,name="ready"),


]
 