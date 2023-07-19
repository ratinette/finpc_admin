from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    post_count = models.IntegerField(default=0)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at


class Board(BaseModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def get_custom_title(self):
        return self.title


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
