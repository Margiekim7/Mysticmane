# Generated by Django 5.1.3 on 2024-12-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysticapp', '0004_message_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
