from django.shortcuts import redirect, HttpResponse, render
from posts.models import Post, Hashtag
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
            'posts': [
                {
                    'id': post.id,
                    'title': post.title,
                    'image': post.image,
                    'rate': post.rate,
                    'hashtags': post.hashtags.all()
                } for post in posts
            ]
        }
        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'posts/hashtags.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post' : post,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)
