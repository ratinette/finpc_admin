# 07. Custom Template Tags

## 07.01 Custom Template Tags 만들기
app 폴더 내 templatetags 폴더 생성

## 07.02 custom_tags.py 생성
```python
# app/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
```

## 07.03 views.py 설정
```python
# app/views.py
from django.shortcuts import render

def template_tag_test(request):
    context = {
        "dict": {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
    }
    return render(request, "template_tag_test.html", context)
```

## 07.04 template_tag_test.html 생성
```html
<!-- app/templates/template_tag_test.html -->
{% load custom_tags %}

{{ dict|get_item:"key1" }}
```

## 07.05 urls.py 설정
```python
# finpc_admin/urls.py
from django.urls import path
from app import views

urlpatterns = [
    ...
    path("template_tag_test/", views.template_tag_test, name="template_tag_test"),
]
```


## 07.06 결과 확인
```bash
python manage.py runserver
```
