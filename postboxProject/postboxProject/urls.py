from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin0317/', admin.site.urls),  # admin url 수정
    path('', include('posts.urls')),
]
