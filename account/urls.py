from django.urls import path, include

from account import views

urlpatterns = [
    # authentication urls
    path('', include('django.contrib.auth.urls')),
    # register
    path('register/', views.register, name='register'),
    # edit
    path('edit/', views.edit, name='edit'),
    # dashboard
    path('', views.dashboard, name='dashboard'),
]
