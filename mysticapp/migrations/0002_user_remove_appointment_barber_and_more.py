# Generated by Django 5.1.3 on 2024-12-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysticapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('yob', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='barber',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='service',
        ),
        migrations.DeleteModel(
            name='Barber',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]