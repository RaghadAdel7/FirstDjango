from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:post_id>/', views.blogdetails, name='blogdetails'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories')
]
