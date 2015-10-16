from django.db import models

# Create your models here.


class Location(models.Model):
    description = models.CharField(max_length=100)

    def natural_key(self):
        return self.description


class Position(models.Model):
    description = models.CharField(max_length=100)

    def natural_key(self):
        return self.description


class SensorType(models.Model):
    description = models.CharField(max_length=50)

    def natural_key(self):
        return self.description


class Sensor(models.Model):
    sensor_type = models.ForeignKey(SensorType)
    location = models.ForeignKey(Location)
    position = models.ForeignKey(Position)

    class Meta:
        abstract = True


class ThermalSensor(Sensor):
    identifier = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now=True)
    time = models.TimeField()
