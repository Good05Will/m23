# Generated by Django 4.2.16 on 2024-09-16 02:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('car_model', models.CharField(max_length=30)),
                ('question', models.TextField(max_length=500)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]