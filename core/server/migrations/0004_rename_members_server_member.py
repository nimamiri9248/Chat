# Generated by Django 4.2.3 on 2023-08-01 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_channel_banner_channel_icon"),
    ]

    operations = [
        migrations.RenameField(
            model_name="server",
            old_name="members",
            new_name="member",
        ),
    ]
