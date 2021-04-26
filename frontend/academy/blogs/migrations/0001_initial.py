# Generated by Django 3.1.7 on 2021-04-09 13:26

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('create_date', models.DateField(default=datetime.datetime(2021, 4, 9, 18, 26, 34, 299556))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='home.TagModel', verbose_name='list_tag')),
            ],
        ),
        migrations.CreateModel(
            name='CommentBlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 4, 9, 13, 26, 34, 302850, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_blog', to='blogs.blogmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyCommentBlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 4, 9, 13, 26, 34, 304159, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment_blog', to='blogs.commentblogmodel')),
            ],
        ),
    ]