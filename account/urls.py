from django.urls import path, include

from account import views

urlpatterns = [
    # authentication urls
    path('', include('django.contrib.auth.urls')),
    # register
    path('register/', views.register, name='register'),
    # users
    path('users/', views.user_list, name='user_list'),
    path('users/follow', views.user_follow, name='user_follow'),
    path('user/<username>', views.user_detail, name='user_detail'),
    # edit
    path('edit/', views.edit, name='edit'),
    # dashboard
    path('', views.dashboard, name='dashboard'),
]
