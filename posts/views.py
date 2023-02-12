from django.shortcuts import redirect, HttpResponse, render
from posts.models import Post
# Create your views here.

def youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')


def hello_view(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)