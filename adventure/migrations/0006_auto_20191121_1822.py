# Generated by Django 3.0rc1 on 2019-11-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adventure", "0005_item_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="room", name="x", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room", name="y", field=models.IntegerField(default=0),
        ),
    ]
