# 03. MySQL 적용 

## 3.1. MySQL 드라이버 설치
```bash
pip install pymysql
```

```python
# settings.py
import pymysql

pymysql.install_as_MySQLdb()
```

## 3.2. settings.py 설정

```python
# settings.py
DATABASES = {
    "default": {
        "NAME": "mt_data",
        "ENGINE": "django.db.backends.mysql",
        "USER": "[USER]",
        "PASSWORD": "[PASSWORD]",  # 계정 비밀번호
        "HOST": "[HOST ADDRESS]",  # 데이테베이스 주소(IP)
        "PORT": [PORT],  # 데이터베이스 포트(보통은 3306)
        "OPTIONS": {
            "autocommit": True,
            "charset": "utf8mb4",
        },
    },
}
```

## 3.3 migrations 폴더 내 파일 삭제
app/migrations 에서 __init__.py 제외 삭제


## 3.4. 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```
