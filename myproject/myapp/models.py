from django.db import models


class Coin(models.Model):
    side = models.CharField(choices=(('О', 'Орел'), ('Р', 'Решка')), max_length=5)
    game_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def coin_throw():
        coin = Coin.objects.all()
        print(coin)
        dict_coin = {'Орел': 0, 'Решка': 0}

        for item in coin:
            if item.side == 'Орел':
                dict_coin['Орел'] += 1
            else:
                dict_coin['Решка'] += 1
        print(dict_coin)
        return dict_coin

    def __repr__(self):
        return f"{self.side}, {self.pk}"

    def __str__(self):
        return f"{self.side}, {self.pk}"
