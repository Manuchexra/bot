# Generated by Django 5.1 on 2024-08-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120)),
                ('first_name', models.TextField(max_length=250)),
                ('last_name', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BotUser',
        ),
    ]