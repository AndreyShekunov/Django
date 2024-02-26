from random import choice, randint

from django.http import HttpResponse

import logging
from .models import Coin, Author

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Страница удачно открылась")
    return HttpResponse("Hello world!")


def game_1(request):
    answer = choice(['Орел', 'Решка'])
    coin = Coin(side=answer)
    coin.save()
    logger.info(f"Ответ: {answer}")
    return HttpResponse(answer)


def static_game(request):
    count = Coin.coin_throw()
    return HttpResponse(f"Орел: {count['Орел']}, Решка: {count['Решка']}")


def view_full_name(request):
    full_name = Author.objects.all()
    result = ''
    for item in full_name:
        result += f"{item.print_full_name()}<br>"
    return HttpResponse(result)


def game_2(request):
    answer = randint(1, 6)
    logger.info(f"Грань кубика: {answer}")
    return HttpResponse(answer)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f"Случайное число: {answer}")
    return HttpResponse(answer)
