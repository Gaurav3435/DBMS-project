from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='home'), #'' refers to home
    path('add',views.add, name='add')
]
