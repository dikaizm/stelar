from django.shortcuts import render

# Create your views here.
def post(request, pk):
    return render(request, 'post.html', {'pk': pk})