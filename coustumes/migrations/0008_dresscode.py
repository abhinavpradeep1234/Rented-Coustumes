# Generated by Django 5.1.3 on 2024-12-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coustumes", "0007_remove_bookingrentedcostumes_item_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DressCode",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("material", models.CharField(blank=True, max_length=200, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("total_stock", models.PositiveIntegerField(blank=True, null=True)),
                ("price", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
