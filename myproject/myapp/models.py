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


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def print_full_name(self):
        return f"{self.name} {self.surname}"


class Posts(models.Model):
    name_title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_watching = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name_title}, {self.author}"
