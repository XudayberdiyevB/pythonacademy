# Generated by Django 3.2 on 2021-05-10 08:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobsmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 10, 8, 18, 49, 920212, tzinfo=utc)),
        ),
    ]
