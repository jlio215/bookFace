# Generated by Django 4.1.1 on 2022-09-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookFaceApp", "0003_rename_user_user_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Account",
        ),
    ]
