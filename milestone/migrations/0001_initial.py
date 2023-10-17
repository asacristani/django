# Generated by Django 4.2.5 on 2023-09-19 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Milestone",
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
                ("slug", models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name="UserMilestone",
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
                ("date", models.DateField()),
                (
                    "milestone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="milestone.milestone",
                    ),
                ),
            ],
        ),
    ]