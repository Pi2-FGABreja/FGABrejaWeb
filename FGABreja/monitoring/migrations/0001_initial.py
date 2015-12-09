# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ThermalSensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('identifier', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField()),
                ('location', models.ForeignKey(to='monitoring.Location')),
                ('position', models.ForeignKey(to='monitoring.Position')),
                ('sensor_type', models.ForeignKey(to='monitoring.SensorType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
