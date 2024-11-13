# Generated by Django 5.1.1 on 2024-10-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swirl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='query_string_to_provider',
            field=models.CharField(default=str, max_length=2048),
        ),
        migrations.AlterField(
            model_name='search',
            name='query_string',
            field=models.CharField(default=str, max_length=2048),
        ),
        migrations.AlterField(
            model_name='search',
            name='query_string_processed',
            field=models.CharField(blank=True, default=str, max_length=2048),
        ),
    ]
