# Generated by Django 3.0 on 2020-02-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimen', '0008_specimen_state_of_decay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eastimages',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='northdetails',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='northimages',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='southdetails',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='southimages',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='specimenepyphyticorganism',
            name='organism',
        ),
        migrations.RemoveField(
            model_name='specimenepyphyticorganism',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='westdetails',
            name='specimen',
        ),
        migrations.RemoveField(
            model_name='westimages',
            name='specimen',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='bark_texture',
            field=models.CharField(choices=[('s', 'Smooth'), ('r', 'Rough')], default='s', max_length=8),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='state_of_decay',
            field=models.CharField(choices=[('i', 'Intact'), ('mi', 'Moderately Intact'), ('l', 'Loose')], default='i', max_length=8),
        ),
        migrations.DeleteModel(
            name='EastDetails',
        ),
        migrations.DeleteModel(
            name='EastImages',
        ),
        migrations.DeleteModel(
            name='EpyphyticOrganism',
        ),
        migrations.DeleteModel(
            name='NorthDetails',
        ),
        migrations.DeleteModel(
            name='NorthImages',
        ),
        migrations.DeleteModel(
            name='SouthDetails',
        ),
        migrations.DeleteModel(
            name='SouthImages',
        ),
        migrations.DeleteModel(
            name='SpecimenEpyphyticOrganism',
        ),
        migrations.DeleteModel(
            name='WestDetails',
        ),
        migrations.DeleteModel(
            name='WestImages',
        ),
    ]
