import json

from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from plotly.offline import plot
from plotly.graph_objs import Scatter
from monitoring.models import TemperatureReading, HumidityReading, TemperatureSensor, HumiditySensor, \
    TemperatureSensorSettings


class IndexView(TemplateView):
    """
    View for all monitoring.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = 'PFA'

        return context


class SettingsView(TemplateView):
    """
    View for monitoring settings.
    """
    template_name = 'settings.html'

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['page_title'] = 'PFA'

        return context


class TemperatureView(TemplateView):
    """
    View for Temperature monitoring.
    """
    template_name = 'temperature.html'

    def get_context_data(self, **kwargs):
        context = super(TemperatureView, self).get_context_data(**kwargs)
        context['page_title'] = 'PFA Temperature'

        return context


class HumidityView(TemplateView):
    """
    View for Humidity monitoring.
    """
    template_name = 'humidity.html'

    def get_context_data(self, **kwargs):
        context = super(HumidityView, self).get_context_data(**kwargs)
        context['page_title'] = 'PFA Humidity'
        humidity_readings = HumidityReading.objects.all()
        dates = []
        values = []
        for humidityReading in humidity_readings:
            dates.append(humidityReading.timestamp)
            values.append(humidityReading.value)
        plot_div = plot([Scatter(x=dates, y=values,
                                 mode='lines', name='Humidity chart',
                                 opacity=0.8, marker_color='#3781d0')],
                        output_type='div')
        context['plot_div'] = plot_div
        context['data'] = humidity_readings

        return context


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            temperature = json_data['temperature']
            humidity = json_data['humidity']
            sensor_name = json_data['sensor']
            measurement_type = json_data['measurement_type']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        HttpResponse("Data was sent successfully!")
        reading = {'sensor': sensor_name, "measurement_type": measurement_type, 'temperature': temperature,
                   'humidity': humidity}
        # TODO: Check if DHT sensor is enabled

        print(reading)

        # Save TemperatureReading to database
        temperature = TemperatureReading()

        for sensor in TemperatureSensor.objects.all():
            if sensor_name[:2] == sensor.name:
                temperature.sensor_id = sensor.id
                for setting in TemperatureSensorSettings.objects.all():
                    if setting.id == sensor.TemperatureSensorSetting_id:
                        sensor_measurement_type = setting.measurement_type
                        temperature.measurement_type = sensor_measurement_type
                        break
                break
        # Conversion to sensor temperature unit
        if measurement_type.capitalize() == sensor_measurement_type:
            temperature.value = reading['temperature']
        elif sensor_measurement_type == 'C':
            temperature.value = int((reading['temperature'] - 32) * 5 / 9)
        else:
            temperature.value = int((reading['temperature'] * 9 / 5) + 32)
        temperature.save()

        # Save HumidityReading to database
        humidity = HumidityReading()
        for sensor in HumiditySensor.objects.all():
            if sensor_name[3:] == sensor.name:
                humidity.sensor_id = sensor.id
                break
        humidity.value = reading['humidity']
        humidity.save()

    return HttpResponse('Data received!')
