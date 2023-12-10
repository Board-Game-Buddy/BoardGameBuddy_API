# Generated by Django 4.2.7 on 2023-12-08 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardgamebuddy_api', '0005_boardgame_cooperative'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userboardgame',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userboardgame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgamebuddy_api.user'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='userboardgame',
            name='board_game_id',
        ),
        migrations.DeleteModel(
            name='BoardGame',
        ),
        migrations.AddField(
            model_name='userboardgame',
            name='board_game_id',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]