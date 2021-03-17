from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


def validate_only_one_instance(Object):
    """
    Validate that only one instance of a model exists.
    """
    model = Object.__class__
    if model.objects.count() > 0 and Object.id != model.objects.get().id:
        raise ValidationError('Only one instance of model %s allowed.' % model.__name__)


def validate_only_one_setting(Object):
    """
    Validate that only one setting of a model exists.
    """
    model = Object.__class__
    if model.objects.count() > 0 and Object.name in model.objects.get().name:
        raise ValidationError('Instances of model %s should be unique.' % model.__name__)


#
### Temperature Sensor, Settings, and Readings
#
class SensorsManager(models.Manager):

    def sensor_list(self, user):
        return HumiditySensor.objects.filter(user=user)


class TemperatureSensor(models.Model):
    """
    Model for Temperature Sensor.
    - type
    - name
    - enabled
    """
    TemperatureSensorSetting = models.ForeignKey(
        'TemperatureSensorSettings', related_name='+',
        blank=True, null=False, default=None, on_delete=models.CASCADE
    )
    TEMP_SENSOR_TYPES = (
        ('DHT11', 'DHT11'),
        ('DHT22', 'DHT22'),
    )
    type = models.CharField(
        choices=TEMP_SENSOR_TYPES,
        max_length=5
    )
    name = models.CharField(
        max_length=30,
        blank=True,
        unique=True
    )
    enabled = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return 'Temperature Sensor ' + str(self.id)

    def clean(self):
        # Only allow one setting of TemperatureSensor model
        # validate_only_one_instance(self)
        pass

    def save(self, *args, **kwargs):
        super(TemperatureSensor, self).save(*args, **kwargs)
        self.full_clean()
        if self.name == '':
            self.name = 'TemperatureSensor ' + str(self.id)
            self.save()


class TemperatureSensorSettings(models.Model):
    """
    Model for Temperature Sensor Settings.
    - sensor (FK)
    - measurement_type
    """

    name = models.CharField(
        max_length=30,
        blank=True,
        unique=True
    )
    MEASUREMENT_TYPES = (
        ('F', 'Fahrenheit'),
        ('C', 'Celsius'),
    )
    measurement_type = models.CharField(
        choices=MEASUREMENT_TYPES,
        max_length=1
    )

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return 'Temperature Sensor Setting ' + str(self.id)

    def clean(self):
        # Only allow one instance of TemperatureSensorSettings model
        # validate_only_one_instance(self)
        pass

    def save(self, *args, **kwargs):
        super(TemperatureSensorSettings, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'TemperatureSensorSetting ' + str(self.id)
            self.save()


class TemperatureReading(models.Model):
    """
    Model for Temperature Reading.
    - sensor (FK)
    - measurement_type
    - timestamp
    - value
    """

    sensor = models.ForeignKey(
        'TemperatureSensor', related_name='+',
        blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    MEASUREMENT_TYPES = (
        ('F', 'Fahrenheit'),
        ('C', 'Celsius'),
    )
    measurement_type = models.CharField(
        choices=MEASUREMENT_TYPES,
        max_length=1
    )
    timestamp = models.DateTimeField(
        default=timezone.now
    )
    value = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )

    def __str__(self):
        return str(self.value)


#
### Humidity Sensor, Settings, and Readings
#

class HumiditySensor(models.Model):
    """
    Model for Humidity Sensor.
    - type
    - name
    - enabled
    """

    HUMID_SENSOR_TYPES = (
        ('D11', 'DHT11'),
        ('D22', 'DHT22'),
    )
    type = models.CharField(
        choices=HUMID_SENSOR_TYPES,
        max_length=3
    )
    name = models.CharField(
        max_length=30,
        blank=True,
        unique=True
    )
    enabled = models.BooleanField(
        default=False
    )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    objects = SensorsManager()

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return 'Humidity Sensor ' + str(self.id)

    """
    def clean(self):
        # Only allow one instance of HumiditySensor model
        validate_only_one_instance(self)
    """

    def save(self, *args, **kwargs):
        super(HumiditySensor, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'HumiditySensor' + str(self.id)
            self.save()


class HumidityReading(models.Model):
    """
    Model for Humidity Reading.
    - sensor (FK)
    - timestamp
    - value
    """

    sensor = models.ForeignKey(
        'HumiditySensor', related_name='+',
        blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        default=timezone.now
    )
    value = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )

    def __str__(self):
        return str(self.value)


#
### Email Alerts
#

class EmailAlert(models.Model):
    """
    Model for Email Alert.
    - timestamp
    - end
    - recipient
    - include_photo
    - min_temperature
    - max_temperature
    - min_humidity
    - max_humidity
    """

    timestamp = models.DateTimeField(
        default=timezone.now
    )
    end = models.DateTimeField()
    recipient = models.EmailField()
    include_photo = models.BooleanField()
    min_temperature = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )
    max_temperature = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )
    min_humidity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    max_humidity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
