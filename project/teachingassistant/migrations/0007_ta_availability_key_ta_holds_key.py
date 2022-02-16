# Generated by Django 4.0.1 on 2022-02-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachingassistant', '0006_alter_availability_friday_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta',
            name='availability_key',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Primary Availability key'),
        ),
        migrations.AddField(
            model_name='ta',
            name='holds_key',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Primary Holds key'),
        ),
    ]