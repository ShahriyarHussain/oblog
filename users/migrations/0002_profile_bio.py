# Generated by Django 3.1.5 on 2021-01-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
