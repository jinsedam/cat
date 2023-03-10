# Generated by Django 4.1.6 on 2023-02-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prec_Au', '0001_initial'),
        ('prec_PEG', '0001_initial'),
        ('prec_Au_PEG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Au',
            field=models.ManyToManyField(blank=True, related_name='Au_PEG', to='prec_Au.info'),
        ),
        migrations.AlterField(
            model_name='info',
            name='PEG',
            field=models.ManyToManyField(blank=True, related_name='Au_PEG', to='prec_PEG.info'),
        ),
    ]
