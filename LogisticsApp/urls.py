from .import views
from django.urls import path


urlpatterns = [
    #LogisticsApp/
    path('', views.LogisticsIndex, name="LogisticsIndex"),

    
    #Logistics/1/2
    path('<int:logistics_id>/', views.logisticsdetailview, name='logisticsdetailview'),
]
