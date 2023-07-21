# 00. 사전 준비

1. [Python 설치](https://www.python.org/downloads/)
2. [Git 설치](https://git-scm.com/downloads)
3. [Visual Studio Code 설치](https://code.visualstudio.com/download)
4. [Visual Studio Code Python Extension 설치](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
5. [Visual Studio Code Git Extension 설치](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
6. Git 학습

## Django 프로젝트 만들기
1. 가상환경 활성화
2. Django 설치
3. Django 프로젝트 생성
4. Django 앱 생성

```bash
pip install django
```

```bash
django-admin startproject my_project .
python manage.py startapp app
```


## settings.py 설정
```python
# settings.py
INSTALLED_APPS = [
    'app.apps.AppConfig',
    ...
]

# or

INSTALLED_APPS = [
    'app',
    ...
]
```
