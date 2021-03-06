# Generated by Django 3.2 on 2021-05-19 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_faqmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqmodel',
            name='answer',
            field=models.TextField(verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faqmodel',
            name='question',
            field=models.TextField(verbose_name='Savol'),
        ),
        migrations.CreateModel(
            name='AdmingaXabar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='usergajavob',
            name='savol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.admingaxabar'),
        ),
        migrations.DeleteModel(
            name='OperatorgaXabar',
        ),
    ]
