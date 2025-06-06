"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from posts.views import text_view, home_page, list_view, detail_view, post_create_view, post_update_view, post_delete_view
from users.views import register_view, login_view, logout_view, profile_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', text_view),
    path('', home_page),
    path('posts/', list_view),
    path('posts/<int:post_id>/', detail_view),
    path('posts/create/', post_create_view),
    path('posts/<int:post_id>/update/', post_update_view),
    path('posts/<int:post_id>/delete/', post_delete_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', profile_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
