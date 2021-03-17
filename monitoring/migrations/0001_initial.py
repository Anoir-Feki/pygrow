# Generated by Django 3.1.7 on 2021-03-16 18:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField()),
                ('recipient', models.EmailField(max_length=254)),
                ('include_photo', models.BooleanField()),
                ('min_temperature', models.IntegerField(validators=[django.core.validators.MinValueValidator(-150), django.core.validators.MaxValueValidator(150)])),
                ('max_temperature', models.IntegerField(validators=[django.core.validators.MinValueValidator(-150), django.core.validators.MaxValueValidator(150)])),
                ('min_humidity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('max_humidity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D11', 'DHT11'), ('D22', 'DHT22')], max_length=3)),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureSensorSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, unique=True)),
                ('measurement_type', models.CharField(choices=[('F', 'Fahrenheit'), ('C', 'Celsius')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DHT11', 'DHT11'), ('DHT22', 'DHT22')], max_length=5)),
                ('name', models.CharField(blank=True, max_length=30, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('TemperatureSensorSetting', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='monitoring.temperaturesensorsettings')),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_type', models.CharField(choices=[('F', 'Fahrenheit'), ('C', 'Celsius')], max_length=1)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(-150), django.core.validators.MaxValueValidator(150)])),
                ('sensor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='monitoring.temperaturesensor')),
            ],
        ),
        migrations.CreateModel(
            name='HumidityReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(-150), django.core.validators.MaxValueValidator(150)])),
                ('sensor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='monitoring.humiditysensor')),
            ],
        ),
    ]