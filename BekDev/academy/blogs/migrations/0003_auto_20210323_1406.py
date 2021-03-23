# Generated by Django 3.1.7 on 2021-03-23 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210323_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 23, 14, 6, 4, 952415)),
        ),
        migrations.AlterField(
            model_name='commentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 9, 6, 4, 955479, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='replycommentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 9, 6, 4, 956480, tzinfo=utc)),
        ),
    ]
