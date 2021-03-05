from faker import Faker

from user.models import User

fake = Faker()


def fake_user(privacy: bool = User.PUBLIC) -> User:
    user = User(username=fake.user_name(), email=fake.email(), privacy=privacy)
    name = fake.name()
    while len(name.split()) == 3:
        name = fake.name()
    user.set_full_name(name)
    user.set_password('abcd')
    user.save()
    return user
