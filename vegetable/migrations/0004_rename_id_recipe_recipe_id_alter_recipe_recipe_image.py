# Generated by Django 4.1.1 on 2023-12-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vegetable", "0003_alter_recipe_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe", old_name="id", new_name="Recipe_id",
        ),
        migrations.AlterField(
            model_name="recipe",
            name="Recipe_image",
            field=models.ImageField(upload_to="Recipe"),
        ),
    ]
