# Generated by Django 5.1 on 2024-08-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_botusers_delete_botuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botusers',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]