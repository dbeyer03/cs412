# Generated by Django 5.1.1 on 2024-10-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octoberone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
