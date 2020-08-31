from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.posts, name='posts'),
    path('recent_posts', views.recent_posts, name='recent_posts'),
    path('count/<str:string>', views.count_str, name='count_str'),
]