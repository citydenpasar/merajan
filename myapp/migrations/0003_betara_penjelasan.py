# Generated by Django 4.1.2 on 2023-04-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_betara'),
    ]

    operations = [
        migrations.AddField(
            model_name='betara',
            name='penjelasan',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
