# Generated by Django 4.1.1 on 2023-12-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vegetable", "0002_recipe_delete_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
