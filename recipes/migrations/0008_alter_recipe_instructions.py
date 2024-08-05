# Generated by Django 4.2.13 on 2024-07-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0007_alter_recipe_instructions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="instructions",
            field=models.TextField(
                default="",
                help_text="number your steps and separate then with a semicolon and a space, like '1. step 1; 2. step 2; 3. step 3'",
                max_length=2000,
            ),
        ),
    ]
