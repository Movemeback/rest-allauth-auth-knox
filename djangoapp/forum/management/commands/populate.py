from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from forum.models import Question, Answer


def create_user(username=None, first_name=None, last_name=None):
    return User.objects.create_user(first_name=first_name or 'Bob', last_name=last_name or 'Bobski',
                                    username=username or 'bob', password='123123')


def create_rob():
    return create_user(username='rob', first_name='Rob')


def create_random_user():
    fake = Faker()
    profile = fake.profile()
    try:
        return User.objects.get(username=profile['username'], first_name=fake.first_name(),
                                last_name=fake.last_name())
    except User.DoesNotExist:
        return create_user(username=profile['username'], first_name=fake.first_name(),
                           last_name=fake.last_name())


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        questions = [
            {'subject': 'Django\'s primary goal is to ease the creation of complex, database-driven websites.',
             'body': fake.text()},
            {'subject': 'The framework emphasizes reusability and "pluggability" of components, less code, ..,',
             'body': fake.text()},
            {'subject': 'Python is used throughout, even for settings files and data models',
             'body': fake.text()},
            {'subject': 'Django also provides an optional administrative create, read, update and delete ...',
             'body': fake.text()},
            {'subject': 'Some well-known sites that use Django include the Public Broadcasting Service,[8] ...',
             'body': fake.text()},
            {'subject': 'It was used on Pinterest,[15] but later the site moved to a framework built over Flask.',
             'body': fake.text()},
        ]

        for question in questions:
            Question.objects.create(subject=question['subject'], body=question['body'], user=create_random_user())

        try:
            rob = User.objects.get(username='rob')
        except User.DoesNotExist:
            rob = create_rob()

        answers = [
            {'body': fake.text()},
            {'body': fake.text()},
            {'body': fake.text()},
            {'body': fake.text()},
            {'body': fake.text()},
            {'body': fake.text()},
            {'body': fake.text()},
        ]

        for answer in answers:
            Answer.objects.create(question=Question.objects.all().order_by('?').first(),
                                  body=answer['body'], user=create_random_user())
