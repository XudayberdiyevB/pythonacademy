# Generated by Django 3.2 on 2021-05-01 11:17

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('create_date', models.DateField(default=datetime.datetime(2021, 5, 1, 16, 17, 21, 806162))),
                ('tag', models.ManyToManyField(to='home.TagModel', verbose_name='tag_list')),
            ],
        ),
    ]
