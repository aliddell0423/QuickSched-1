# Generated by Django 4.0.1 on 2022-02-17 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingassistant', '0008_alter_holds_ta_alter_holds_update_availability_and_more'),
        ('laborganizer', '0002_lab_assigned_tas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='assigned_tas',
        ),
        migrations.AddField(
            model_name='lab',
            name='assigned_ta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teachingassistant.ta'),
        ),
    ]
