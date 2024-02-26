from django.core.management.base import BaseCommand

from myapp.models import Author


class Command(BaseCommand):
    help = "Создание авторов путём генерации "

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            author = Author(name=f'Name{i}',
                            surname=f'Surname{i}',
                            email=f'mail{i}@mail.ru',
                            biography=f'биография{i}',
                            birthday=f'2000-01-0{i}')
            author.save()
