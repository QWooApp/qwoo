from faker import Faker

from random import choice

from user.models import User
from blog.models import Post

fake = Faker()

USER_IDS = User.objects.values_list('id', flat=True)


def fake_post() -> Post:
    return Post.objects.create(
        body=fake.text(300),
        user_id=choice(USER_IDS),
    )
