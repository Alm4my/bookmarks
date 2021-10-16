from django.urls import path

from account import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]
