from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('М', 'Монета'), ('К', 'Кость'), ('Ч', 'Случайное число')])
    number = forms.IntegerField(min_value=1, max_value=64)



