from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from app.models import Post

def index(request):
    data = Post.objects.all()  # 쿼리셋 예시
    return render(request, "index.html", {"posts": data})
