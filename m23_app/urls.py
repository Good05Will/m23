from django.urls import path
from . import views

app_name = 'm23_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_order', views.new_order, name='new_order'),
    path('services', views.services, name='services'),
    path('about_us', views.about_us, name='about_us'),
    path('contacts', views.contacts, name='contacts'),
]
