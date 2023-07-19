# 01. 모델 정의하기

## 모델 정의
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    post_count = models.IntegerField(default=0)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Board(BaseModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField(User, related_name="likes", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

```

## settings.py 인증 유저모델 변경
```python
# settings.py
AUTH_USER_MODEL = "app.User"
```

## admin.py 등록
```python
# admin.py
from django.contrib import admin
from app.models import User, Board, Post, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
```

## 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

## 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

## 서버 실행
```bash
python manage.py runserver
```

## 관리자 페이지 접속
http://localhost:8000/admin
