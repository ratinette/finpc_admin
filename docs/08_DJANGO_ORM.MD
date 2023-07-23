# 08. Django ORM 심화

## 08.01 Query Set 만들기 심화
1. Min(), Max(), Avg(), Count()
2. F() 객체
3. select_related()
4. prefetch_related()

Post 모델에 like_count 추가
```python
# models.py
class Post(models.Model):
    ...
    like_count = models.IntegerField(default=0)
```

## 08.02 Min(), Max(), Avg(), Count() 예시
```python
# views.py
from django.shortcuts import render
from django.db.models import Min, Max, Avg, Count
from app.models import Post

def post_view(request, post_id):
    min_likes = Post.objects.aggregate(Min('like_count'))
    max_likes = Post.objects.aggregate(Max('like_count'))
    avg_likes = Post.objects.aggregate(Avg('like_count'))
    count_likes = Post.objects.aggregate(Count('id'))

    context = {
        'min_likes': min_likes,
        'max_likes': max_likes,
        'avg_likes': avg_likes,
        'count_likes': count_likes,
    }

    return render(request, 'post_stat.html', context)
```

```python
# urls.py
from django.urls import path
from app.views import post_view

urlpatterns = [
    path('posts/stats/', post_view),
]
```

```html
<!-- post_stat.html -->
<h1>Post Stat</h1>
<p>Min Likes: {{ min_likes }}</p>
<p>Max Likes: {{ max_likes }}</p>
<p>Avg Likes: {{ avg_likes }}</p>
<p>Count Likes: {{ count_likes }}</p>
```

## 08.03 F() 객체 예시
```python
# views.py
from django.shortcuts import render
from django.db.models import F
from app.models import Post
    
def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like_count = F('like_count') + 1
    post.save()
    return render(request, 'post_like.html')
```

```python
# urls.py
from django.urls import path
from app.views import post_view

urlpatterns = [
    path('posts/<int:post_id>/', post_view),
]
```

```html
<!-- post_like.html -->
<h1>Post Stat</h1>
<p>Like Count: {{ post.like_count }}</p>
<p>Post Title: {{ post.title }}</p>
```

## 08.04 select_related() 예시
```python
# views.py
from django.shortcuts import render
from app.models import Post, Comment

def comment_view(request):
    comments = Comment.objects.select_related('post')
    context = {
        'comments': comments,
    }
    return render(request, 'comment_view.html', context)
```

```python
# urls.py
from django.urls import path
from app.views import comment_view

urlpatterns = [
    path('comments/', comment_view),
]
```

```html
<!-- comment_view.html -->
<h1>Comment View</h1>
{% for comment in comments %}
    <p>Post Title: {{ comment.post.title }}</p>
    <p>Comment Content: {{ comment.content }}</p>
{% endfor %}
```

## 08.05 prefetch_related() 예시
```python
# views.py
from django.shortcuts import render
from app.models import Post, Comment

def post_view_prefetch(request, post_id):
    post = Post.objects.filter(id=post_id).prefetch_related('comment_set')
    context = {
        'post': post,
    }
    return render(request, 'post_view_prefetch.html', context)
```

```python
# urls.py
from django.urls import path
from app.views import post_view_prefetch

urlpatterns = [
    path('posts/<int:post_id>/prefetch/', post_view_prefetch),
]
```

```html
<!-- post_view_prefetch.html -->
<h1>Post View Prefetch</h1>
{% for comment in post.comment_set.all %}
    <p>Comment Content: {{ comment.content }}</p>
{% endfor %}
```
