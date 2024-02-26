from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game_1/', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3'),
    path('static_game/', views.static_game, name='static_game')
]