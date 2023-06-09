# Generated by Django 4.1.7 on 2023-03-18 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='main_app/static/uploads')),
                ('appointments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.appointments')),
            ],
        ),
    ]
