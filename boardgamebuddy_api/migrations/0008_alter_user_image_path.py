# Generated by Django 4.2.7 on 2023-12-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgamebuddy_api', '0007_user_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_path',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
