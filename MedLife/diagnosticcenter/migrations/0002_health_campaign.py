# Generated by Django 4.0.6 on 2022-08-26 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticcenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health_Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campaign_Name', models.CharField(max_length=100)),
                ('Organizer_name', models.CharField(max_length=45)),
                ('Venue', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
