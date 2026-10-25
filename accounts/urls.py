"""defines URL pattern for the account"""

from django.urls import path, include

from . import views



app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #register page
    path('register', views.register, name='register'),
]