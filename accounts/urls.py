from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
    path('register.html', views.registerPage, name="register2"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('dashboard/', views.dashboard, name="dashboard"), 
	path('profile', views.profile, name="profile"),
	path('editprofile', views.editprofile, name="editprofile"),
  
    # path('customer/<str:pk_test>/', views.customer, name="customer"),



]
