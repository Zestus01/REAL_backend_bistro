from django.urls import path
from . import views


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cuisine/<int:cuisine_id>/', views.Cuisine, name='Cuisine'),
    path('menu/', views.get_menu),
]