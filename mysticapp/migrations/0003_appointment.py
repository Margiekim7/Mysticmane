# Generated by Django 5.1.3 on 2024-12-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysticapp', '0002_user_remove_appointment_barber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('stylist', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
