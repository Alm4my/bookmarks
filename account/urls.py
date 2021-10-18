from django.urls import path, include
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    # authentication urls
    path('', include('django.contrib.auth.urls')),
    # dashboard
    path('', views.dashboard, name='dashboard'),
]
