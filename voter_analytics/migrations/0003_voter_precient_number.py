# Generated by Django 5.1.1 on 2024-11-12 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0002_alter_voter_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='precient_number',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]