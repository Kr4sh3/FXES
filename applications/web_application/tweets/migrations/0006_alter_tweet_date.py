# Generated by Django 5.0.3 on 2024-03-05 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_alter_tweet_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 17, 5, 10, 338622), verbose_name='date published'),
        ),
    ]
