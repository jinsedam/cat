# Generated by Django 4.1.6 on 2023-02-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('sample_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('MPEG_input_amount', models.FloatField(blank=True, null=True)),
                ('TGA_input_amount', models.FloatField(blank=True, null=True)),
                ('Toluene_input_amount', models.FloatField(blank=True, null=True)),
                ('operating_temperature', models.FloatField(blank=True, null=True)),
                ('operating_RPM', models.FloatField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('duration_time', models.TimeField(blank=True, null=True)),
                ('taget_amount', models.FloatField(blank=True, null=True)),
                ('real_output_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Information',
            },
        ),
    ]
