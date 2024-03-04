from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game_1/', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3'),
    path('static_game/', views.static_game, name='static_game'),
    path('view_full_name/', views.view_full_name, name='view_full_name'),
    path('about/', views.about, name='about'),
    path('author/<int:author_id>', views.show_posts, name='show_posts'),
    path('post/<int:post_id>', views.show_post_id, name='show_post_id'),
    path('games_form/', views.choice_games, name='choice_games'),
]
