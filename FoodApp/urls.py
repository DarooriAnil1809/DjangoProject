from .import views
from django.urls import path


urlpatterns = [
    #FoodApp/
    path('', views.index, name="index"),

    #FoodApp/1/2
    path('<int:item_id>/', views.detailview, name='detailview'),

    #To Create New ITEM from forms /FoodApp/
    path('add', views.create_item, name="create_item"),

    #Edit and Update Items
    path('update/<int:id>/', views.update_item, name="update_item"),

    #To Delete the Items
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
    
]
