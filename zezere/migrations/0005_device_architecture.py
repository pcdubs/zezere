# Generated by Django 2.2.6 on 2019-10-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("zezere", "0004_auto_20191018_0822")]

    operations = [
        migrations.AddField(
            model_name="device",
            name="architecture",
            field=models.CharField(
                default="x86_64", max_length=50, verbose_name="Architecture"
            ),
            preserve_default=False,
        )
    ]
