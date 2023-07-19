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
