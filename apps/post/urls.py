from . import views
from django.urls import path

urlpatterns = [
    path('post/<str:pk>', views.post, name='post')
]