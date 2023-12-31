# Generated by Django 4.2.3 on 2023-07-22 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parameter",
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
                ("name", models.CharField(max_length=30)),
                ("value", models.CharField(max_length=20)),
                (
                    "created_day",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]
