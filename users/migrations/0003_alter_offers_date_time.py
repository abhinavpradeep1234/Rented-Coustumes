# Generated by Django 5.1.3 on 2024-12-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_offers_customuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offers",
            name="date_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
