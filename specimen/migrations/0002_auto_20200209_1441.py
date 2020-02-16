# Generated by Django 3.0 on 2020-02-09 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('specimen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='score',
            new_name='ph_level',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='collection_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]