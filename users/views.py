from django.shortcuts import render, redirect


# Create your views here.
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, DetailView
from posts.models import Post
from posts.forms import PostCreateForm





class RegisterCBV(ListView, CreateView):
    model = Post
    template_name = 'users/register.html'

    def get(self, request, **kwargs):
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'пароли не совпадают!')
        return render(request, 'users/register.html', context={
            'form': form
        })


class LoginCBV(ListView):
    template_name = 'users/login.html'

    def get(self, request, **kwargs):
        context = {
            'form': LoginForm
        }

        return render(request, 'users/login.html', context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            """authenticate"""
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error('username', 'пользователь не найден')

        return render(request, 'users/login.html', context={
            'form': form
        })


class LogoutCBV(ListView):
    def get(self, request):
        logout(request)
        return redirect('/posts/')


