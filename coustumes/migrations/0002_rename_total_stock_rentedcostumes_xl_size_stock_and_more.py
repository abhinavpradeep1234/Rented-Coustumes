# Generated by Django 5.1.3 on 2024-12-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coustumes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rentedcostumes",
            old_name="total_stock",
            new_name="XL_size_stock",
        ),
        migrations.AddField(
            model_name="rentedcostumes",
            name="XXL_size_stock",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="rentedcostumes",
            name="large_size_stock",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="rentedcostumes",
            name="medium_size_stock",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="rentedcostumes",
            name="small_size_stock",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
