from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('name',views.name, name='name'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    
]