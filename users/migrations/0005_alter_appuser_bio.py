# Generated by Django 4.2.13 on 2024-07-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_appuser_bio_appuser_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='bio',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
