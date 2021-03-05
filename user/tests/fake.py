from faker import Faker

from user.models import User

fake = Faker()


def fake_user(privacy: bool = User.PUBLIC) -> User:
    return User.objects.create_user(
        password='abcd',
        privacy=privacy,
        email=fake.email(),
        username=fake.user_name(),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
    )
