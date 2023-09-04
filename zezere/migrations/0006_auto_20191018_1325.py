# Generated by Django 2.2.6 on 2019-10-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("zezere", "0005_device_architecture")]

    operations = [
        migrations.AddField(
            model_name="runrequest",
            name="efi_application",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="EFI Application path",
            ),
        ),
        migrations.AddField(
            model_name="runrequest",
            name="type",
            field=models.CharField(
                choices=[("ok", "Online kernel"), ("ef", "EFI application")],
                default="ok",
                max_length=2,
                verbose_name="RunRequest type",
            ),
            preserve_default=False,
        ),
    ]
