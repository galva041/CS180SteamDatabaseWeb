# Generated by Django 4.0.4 on 2022-05-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0005_alter_games_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='game_id',
        ),
    ]
