from django.urls import path
from . import views

app_name= 'pages'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('contact/', views.contact, name='contact'),

]
