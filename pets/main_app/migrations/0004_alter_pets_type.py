# Generated by Django 4.1.7 on 2023-03-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='type',
            field=models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], max_length=2),
        ),
    ]