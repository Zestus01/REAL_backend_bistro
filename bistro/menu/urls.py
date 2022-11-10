from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu),
    
    path('cuisine/<int:cuisine_id>/', views.Cuisine, name='Cuisine'),
]