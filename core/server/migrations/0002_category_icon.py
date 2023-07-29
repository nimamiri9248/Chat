# Generated by Django 4.2.3 on 2023-07-29 14:00

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.FileField(
                blank=True, null=True, upload_to=server.models.category_icon_upload_path
            ),
        ),
    ]
