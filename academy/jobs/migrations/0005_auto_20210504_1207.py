# Generated by Django 3.2 on 2021-05-04 07:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210504_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 7, 7, 1, 647128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobsmodel',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]