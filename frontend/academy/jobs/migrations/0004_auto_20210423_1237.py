# Generated by Django 3.1.7 on 2021-04-23 07:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210414_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 7, 37, 6, 953447, tzinfo=utc)),
        ),
    ]