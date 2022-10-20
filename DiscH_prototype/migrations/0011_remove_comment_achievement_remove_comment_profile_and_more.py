# Generated by Django 4.0.4 on 2022-10-15 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiscH_prototype', '0010_comment_achievement_comment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='achievement',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 5)),
        ),
        migrations.AlterField(
            model_name='answer_bow',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 25)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 5)),
        ),
    ]