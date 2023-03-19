from . import views
from django.urls import path

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('blog/post', views.post, name='post'),
    path('blog/author', views.author, name='author')
]