from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.newPost, name='newPost'),
    path('analytics', views.analytics, name='analytics'),
    path('user/<int:id>', views.user_detail, name='user_detail'),
]
