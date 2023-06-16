from .import views
from django.urls import path


urlpatterns = [
    #MusicApp/
    path('', views.MusicIndex, name="MusicIndex"),

        
]
