# Generated by Django 3.1.5 on 2021-02-04 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210204_2346'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comments',
            name='pk_comment',
        ),
    ]
