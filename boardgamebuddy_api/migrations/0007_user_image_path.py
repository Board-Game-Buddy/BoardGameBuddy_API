# Generated by Django 4.2.7 on 2023-12-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgamebuddy_api', '0006_remove_userboardgame_user_id_userboardgame_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_path',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]
