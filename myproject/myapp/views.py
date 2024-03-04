from random import choice, randint

from django.http import HttpResponse

import logging

from django.shortcuts import render

from .form import GameForm, AuthorForm
from .models import Coin, Author, Posts

logger = logging.getLogger(__name__)


def index(request):
    logger.info("'Главная' страница удачно открылась")
    return render(request, "myapp/index.html")


def about(request):
    logger.info("Страница 'О нас' удачно открылась")
    return render(request, "myapp/about.html")


def game_1(request):
    answer = choice(['Орел', 'Решка'])
    coin = Coin(side=answer)
    coin.save()
    logger.info(f"Ответ: {answer}")
    context = {'result': answer}
    return render(request, "myapp/games.html", context)


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
    context = {'result': answer}
    return render(request, "myapp/games.html", context)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f"Случайное число: {answer}")
    context = {'result': answer}
    return render(request, "myapp/games.html", context)


def show_posts(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Posts.objects.filter(author=author)

    context = {'posts': posts}
    return render(request, "myapp/posts.html", context)


def show_post_id(request, post_id):
    post = Posts.objects.get(pk=post_id)

    context = {'post': post}
    return render(request, "myapp/post.html", context)


def choice_games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.data['game']
            number = form.data['number']
            if game == 'К':
                return game_2(request)
            elif game == 'М':
                return game_1(request)
            elif game == 'Ч':
                return game_3(request)
    else:
        form = GameForm()
    # print(form)
    return render(request, "myapp/games_form.html", {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            surname = form.data['surname']
            email = form.data['email']
            biography = form.data['biography']
            birthday = form.data['birthday']
            author = Author(name=name, surname=surname, email=email, biography=biography, birthday=birthday)
            author.save()
    else:
        form = AuthorForm()
    return render(request, "myapp/add_author.html", {'form': form})