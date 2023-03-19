from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def author(request):
    return render(request, 'author.html')