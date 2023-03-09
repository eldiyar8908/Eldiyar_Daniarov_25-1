"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import MainPageCBV, PostsCBV, HashtagsCBV, CreatePostCBV, PostDetailCBV, post_detail_view
from users.views import RegisterCBV, LoginCBV, LogoutCBV
from django.conf.urls.static import static
from blog.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostsCBV.as_view()),
    path('posts/', PostsCBV.as_view()),
    path('', MainPageCBV.as_view()),
    path('hashtags/', HashtagsCBV.as_view()),
    path('posts/create/', CreatePostCBV.as_view()),
    path('posts/<int:id>/', PostDetailCBV.as_view()),
    # path('posts/<int:pk>/', PostDetailCBV.as_view()),
    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view())
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
