from django.urls import path

from images import views

app_name = 'images'

urlpatterns = [
    path('', views.image_list, name='list'),
    path('ranking/', views.image_ranking, name='ranking'),
    path('create/', views.image_create, name='create'),
    path('like/', views.image_like, name='like'),
    path('detail/<int:image_id>/<slug:slug>', views.image_detail, name='detail'),
]
