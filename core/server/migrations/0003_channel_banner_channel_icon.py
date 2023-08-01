# Generated by Django 4.2.3 on 2023-08-01 07:59

from django.db import migrations, models
import server.models
import server.validators


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0002_category_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=server.models.server_banner_upload_path,
                validators=[server.validators.validate_image_file_exstension],
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=server.models.server_icon_upload_path,
                validators=[
                    server.validators.validate_icon_image_size,
                    server.validators.validate_image_file_exstension,
                ],
            ),
        ),
    ]
