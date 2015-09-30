from django.db import models

# Create your models here.


class Location(models.Model):
    description = models.CharField(max_length=100)


class Position(models.Model):
    description = models.CharField(max_length=100)


class SensorType(models.Model):
    description = models.CharField(max_length=50)


class Sensor(models.Model):
    sensor_type = models.ForeignKey(SensorType)
    location = models.ForeignKey(Location)
    position = models.ForeignKey(Position)

    class Meta:
        abstract = True


class TermalSensor(Sensor):
    temperature = models.FloatField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
