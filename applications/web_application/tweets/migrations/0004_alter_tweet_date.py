# Generated by Django 5.0.3 on 2024-03-05 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_date_alter_tweet_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 15, 33, 33, 742181), verbose_name='date published'),
        ),
    ]