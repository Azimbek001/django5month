# Generated by Django 4.2.3 on 2023-08-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 'Очень плохо'), (2, 'Плохо'), (3, 'Средне'), (4, 'Хорошо'), (5, 'Отлично')], default=5),
        ),
    ]
