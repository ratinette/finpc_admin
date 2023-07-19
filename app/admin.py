from django.contrib import admin
from app.models import User, Board, Post, Comment


admin.site.site_header = "My admin"


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class BoardModelAdmin(admin.ModelAdmin):
    list_display = ("title_", "created_at_")
    list_filter = ("created_at",)
    search_fields = ("title",)
    inlines = [PostInline]

    def title_(self, obj):
        return obj.title

    def created_at_(self, obj):
        return obj.created_at

    title_.short_description = "제목"
    created_at_.short_description = "생성 시간"


# Register your models here.
admin.site.register(User)
admin.site.register(Board, BoardModelAdmin)
admin.site.register(Post)
admin.site.register(Comment)
