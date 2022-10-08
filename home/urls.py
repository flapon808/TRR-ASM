from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('weekly_offers/',views.weekly,name="weeklyoffers"),
    
]
