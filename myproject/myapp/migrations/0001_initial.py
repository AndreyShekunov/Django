# Generated by Django 5.0.2 on 2024-02-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('О', 'Орел'), ('Р', 'Решка')], max_length=5)),
                ('game_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
