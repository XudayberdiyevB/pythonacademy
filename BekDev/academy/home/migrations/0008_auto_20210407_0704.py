# Generated by Django 3.1.7 on 2021-04-07 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210406_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 7, 3, 59, 118120)),
        ),
    ]
