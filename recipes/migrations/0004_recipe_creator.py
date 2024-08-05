# Generated by Django 4.2.13 on 2024-07-08 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_appuser_bio_appuser_pic'),
        ('recipes', '0003_alter_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.appuser'),
        ),
    ]
