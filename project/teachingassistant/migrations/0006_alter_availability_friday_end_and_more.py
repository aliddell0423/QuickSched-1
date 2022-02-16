# Generated by Django 4.0.1 on 2022-02-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachingassistant', '0005_alter_availability_friday_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='friday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='friday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='monday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='monday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='saturday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='saturday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='sunday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='sunday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='thursday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='thursday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='tuesday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='tuesday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='wednesday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='wednesday_start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]