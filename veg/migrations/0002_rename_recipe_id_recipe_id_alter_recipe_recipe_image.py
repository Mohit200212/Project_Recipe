# Generated by Django 4.1.1 on 2023-12-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("veg", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe", old_name="Recipe_id", new_name="id",
        ),
        migrations.AlterField(
            model_name="recipe",
            name="Recipe_image",
            field=models.ImageField(upload_to="public"),
        ),
    ]
