# 07. Django Cache Framework

## 07.01 Django Cache Framework의 종류
1. 전체 페이지 캐시
2. 뷰단위 캐시
3. 템플릿 조각 캐시
4. QuerySet 캐시


## 07.02 캐시 사용하기
1. settings.py 설정
```python
# settings.py에 추가
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

2. 뷰단위 캐시
```python
# views.py
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index(request):
    return render(request, 'index.html')
```


3. 템플릿 조각 캐시
```python
# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

```html
<!-- index.html -->
{% load cache %}
{% cache 500 sidebar %}
    .. sidebar ..
{% endcache %}
```

4. QuerySet 캐시
```python
# views.py
from django.core.cache import cache
from app.models import Post
from django.shortcuts import render


def index(request):
    data = cache.get('all_posts')
    if data is None:
        # 캐시가 없으면 데이터베이스에서 데이터를 가져와서 캐시에 저장
        data = Post.objects.all()  # 쿼리셋 예시
        cache.set('all_posts', data, timeout=3600)  # 3600초(1시간) 동안 캐시 저장
    return render(request, "index.html", {"posts": data})
```

```html
{% for p in posts %}
  <h1>{{ p.title }}</h1>
  <p>{{ p.content }}</p>
{% endfor %}
```
