# Generated by Django 3.0 on 2020-02-16 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specimen', '0004_auto_20200216_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eastimages',
            name='details',
        ),
        migrations.RemoveField(
            model_name='northimages',
            name='details',
        ),
        migrations.RemoveField(
            model_name='southimages',
            name='details',
        ),
        migrations.RemoveField(
            model_name='westimages',
            name='details',
        ),
        migrations.AddField(
            model_name='eastimages',
            name='specimen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='specimen.Specimen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='northimages',
            name='specimen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='specimen.Specimen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='southimages',
            name='specimen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='specimen.Specimen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='westimages',
            name='specimen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='specimen.Specimen'),
            preserve_default=False,
        ),
    ]
