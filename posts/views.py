from django.shortcuts import redirect, render
from posts.models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from posts.constants import PAGINATION_LIMIT
from django.views.generic import ListView, CreateView, DetailView





class MainPageCBV(ListView):
    model = Post
    template_name = "layouts/index.html"


class PostsCBV(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get(self, request, **kwargs):
        posts = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get("page", 1))

        if search:
            posts = posts.filter(title__contains=search) | posts.filter(description__contains=search)

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'posts': [
                {
                    'id': post.id,
                    'title': post.title,
                    'image': post.image,
                    'rate': post.rate,
                    'hashtags': post.hashtags.all()
                } for post in posts
            ],
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context)


class HashtagsCBV(ListView):
    model = Hashtag
    template_name = 'posts/hashtags.html'

    def get(self, request, **kwargs):
        hashtags = self.get_queryset()

        context = {
            'hashtags': hashtags
        }

        return render(request, self.template_name, context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'form': CommentCreateForm
        }

        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        data = request.POST
        form = CommentCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
            )

        context = {
            'post': post,
            'comments': post.comments.all,
            'form': form
        }






class PostDetailCBV(DetailView, CreateView):
    model = Post
    template_name = 'posts/detail.html'
    form_class = CommentCreateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'post': self.get_object(),
            'comments': Comment.objects.filter(post=self.get_object()),
            'form': kwargs.get('form', self.form_class)
        }

    def post(self, request, **kwargs):
        data = request.POST
        form = CommentCreateForm(data=data)

        if form.is_valid():
            Post.objects.create(
                text=form.cleaned_data.get('text'),
                rate=form.cleaned_data.get('rate'),
                post_id=self.get_object().id
            )
            return redirect(f'/posts/{self.get_object().id}/')

        return render(request, self.template_name, context=self.get_context_data(
            form=form
        ))


class CreatePostCBV(ListView, CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': self.form_class if not kwargs.get('form') else kwargs['form']
        }

    def get (self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, *args, **kwargs):
        data, files = request.POST, request.FILES

        form = PostCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/posts')

        return render(request, 'posts/create.html', context={
            'form': form
        })




