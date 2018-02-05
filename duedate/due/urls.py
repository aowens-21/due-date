from django.urls import path

from . import views

app_name = 'due'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_assignment, name='create_assignment'),
]
