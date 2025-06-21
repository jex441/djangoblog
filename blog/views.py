from django.shortcuts import render
from django.http import HttpResponse

posts = [
      {
            'author': 'Jeff W',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'Jun 10 2025'
      },
       {
            'author': 'Jeff W',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'Jun 11 2025'
      },
]

# Create your views here.
def home(request):
    context = {
          'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
       return render(request, 'blog/about.html', {'title': 'About'})
