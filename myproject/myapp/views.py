from random import choice, randint

from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Страница удачно открылась")
    return HttpResponse("Hello world!")


def game_1(request):
    answer = choice(['Орел', 'Решка'])
    logger.info(f"Ответ: {answer}")
    return HttpResponse(answer)


def game_2(request):
    answer = randint(1, 6)
    logger.info(f"Грань кубика: {answer}")
    return HttpResponse(answer)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f"Случайное число: {answer}")
    return HttpResponse(answer)
