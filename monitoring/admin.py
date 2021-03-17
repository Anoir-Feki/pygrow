from django.contrib import admin

import monitoring.models as models

admin.site.register(models.TemperatureSensor)
admin.site.register(models.TemperatureSensorSettings)
admin.site.register(models.TemperatureReading)
admin.site.register(models.HumiditySensor)
admin.site.register(models.HumidityReading)
admin.site.register(models.EmailAlert)
