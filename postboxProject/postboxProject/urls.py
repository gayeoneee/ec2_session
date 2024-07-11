from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin0317/', admin.site.urls),  # admin url 수정
    path('', include('postapp.urls')),  # 앱의 urls를 받아오는 것
]

handler404 = page_not_found