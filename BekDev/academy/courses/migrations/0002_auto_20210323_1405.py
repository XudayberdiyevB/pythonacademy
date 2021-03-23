# Generated by Django 3.1.7 on 2021-03-23 09:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursevideomodel',
            name='file',
        ),
        migrations.RemoveField(
            model_name='coursevideomodel',
            name='video_name',
        ),
        migrations.RemoveField(
            model_name='coursevideomodel',
            name='video_time',
        ),
        migrations.AddField(
            model_name='coursevideomodel',
            name='video_url',
            field=models.URLField(default='https://www.google.com/'),
        ),
        migrations.AlterField(
            model_name='commentcourse',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 9, 5, 25, 580903, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courselistmodel',
            name='date_of_kurs',
            field=models.DateField(default=datetime.datetime(2021, 3, 23, 14, 5, 25, 574905)),
        ),
        migrations.AlterField(
            model_name='replycommentcourse',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 9, 5, 25, 581899, tzinfo=utc)),
        ),
    ]
