# 06. BG Scheduler

## 06.01 APScheduler & Faker 설치
    
```bash
pip install apscheduler
pip install Faker
```

## 06.02 scheduler 폴더생성
app/scheduler 폴더를 생성한다.

## 06.03 scheduler.py 생성
app/scheduler/scheduler.py 파일을 생성한다.
app/scheduler/db_connector.py 파일을 생성한다.
app/scheduler/__init__.py 파일을 생성한다.

## 06.04 __.py 설정

```python
# settings.py
from app.scheduler.create_random_post import *
from apscheduler.schedulers.background import BackgroundScheduler


def cron_jobs():
    print("JOB Started")
    sched = BackgroundScheduler()
    sched.add_job(create_random_post, "interval", minutes=1)

    sched.start()

```

## 06.05 scheduler.py 설정

```python
from app.models import Post, Board, User
from app.scheduler.db_connector import db_auto_reconnect
from faker import Faker
import random


@db_auto_reconnect
def create_random_post():
    print("new post created")
    get_board_ids = Board.objects.values_list("id", flat=True)
    get_author_ids = User.objects.values_list("id", flat=True)
    get_board_ids = list(get_board_ids)
    get_author_ids = list(get_author_ids)

    if not get_board_ids or not get_author_ids:
        return

    fake = Faker("ko_KR")
    new_post = Post()
    new_post.title = fake.sentence()
    new_post.content = fake.text()
    new_post.board_id = random.choice(get_board_ids)
    new_post.author_id = random.choice(get_author_ids)

    new_post.save()
```

## 06.06 db_connector.py 설정

```python
from functools import wraps

from django.db import connection


def db_auto_reconnect(func):
    """Auto reconnect db when mysql has gone away."""

    @wraps(func)
    def wrapper(*args, **kwagrs):
        try:
            connection.connection.ping()
        except Exception:
            connection.close()
        return func(*args, **kwagrs)

    return wrapper
```
