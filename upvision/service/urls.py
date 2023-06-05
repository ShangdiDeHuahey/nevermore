from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('documentation', views.documentation, name='documentation'),
    path('contacts', views.contacts, name='contacts'),
]