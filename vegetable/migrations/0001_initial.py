# Generated by Django 4.1.1 on 2023-12-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("discription", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="")),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
