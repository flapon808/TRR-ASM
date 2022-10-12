from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('weekly_meals/',views.weekly,name="weeklymeals"),
    path('restaurants/',views.restaurants,name="restaurants"),

    
]
