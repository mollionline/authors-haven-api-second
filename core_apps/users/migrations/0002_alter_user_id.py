# Generated by Django 3.2.11 on 2023-03-07 16:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ee297a01-4ace-41ec-bce7-abcdcf90fd0b'), editable=False, unique=True),
        ),
    ]
