# Generated by Django 3.1.5 on 2021-01-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210123_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(default='Hi!', max_length=100),
        ),
    ]
