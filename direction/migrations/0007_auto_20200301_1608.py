# Generated by Django 3.0 on 2020-03-01 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0006_auto_20200301_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eastdetails',
            old_name='ph_level',
            new_name='ph_level_1',
        ),
        migrations.RenameField(
            model_name='northdetails',
            old_name='ph_level',
            new_name='ph_level_1',
        ),
        migrations.RenameField(
            model_name='southdetails',
            old_name='ph_level',
            new_name='ph_level_1',
        ),
        migrations.RenameField(
            model_name='westdetails',
            old_name='ph_level',
            new_name='ph_level_1',
        ),
    ]
