# Generated by Django 3.1.7 on 2021-04-23 07:37

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210414_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 23, 12, 37, 6, 388613)),
        ),
        migrations.AlterField(
            model_name='cardmodel',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]