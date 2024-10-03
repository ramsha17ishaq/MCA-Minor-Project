# Generated by Django 4.0.6 on 2022-08-26 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticcenter', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostName', models.CharField(max_length=30)),
                ('NoOfseats', models.IntegerField()),
                ('Lastdatetoapply', models.DateField(default=django.utils.timezone.now)),
                ('Postdate', models.DateField(default=django.utils.timezone.now)),
                ('Description', models.TextField()),
            ],
        ),
    ]
