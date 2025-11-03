from django.urls import path
from .views import *
from .auth_views import login,logout,regis

urlpatterns = [
    path('',index,name='home'),
    path('add_food/',add_food,name="add-food"),
    path('add_category/',add_category,name="add-category"),

    #auth
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('regis/',regis, name ='regis'),
]