# Generated by Django 3.0 on 2020-03-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0005_auto_20200301_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='eastdetails',
            name='ph_level_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='eastdetails',
            name='ph_level_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='northdetails',
            name='ph_level_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='northdetails',
            name='ph_level_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='southdetails',
            name='ph_level_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='southdetails',
            name='ph_level_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='westdetails',
            name='ph_level_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='westdetails',
            name='ph_level_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='eastimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specimen_images/east/'),
        ),
        migrations.AlterField(
            model_name='northimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specimen_images/north/'),
        ),
        migrations.AlterField(
            model_name='southimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specimen_images/south/'),
        ),
    ]