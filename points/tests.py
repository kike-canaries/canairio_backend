from random import randint
from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase


class FixedStationTestCase(APITestCase):

    def setUp(self):
        self.username = 'thing'
        self.password = 'thong'
        self.email = 'me@he.re'
        self.maxpm25 = 501
        self.sensorid = 'D714E1CC605C'
        self.sensorname = 'myhomecanair'
        self.user = User.objects.create_user(
            self.username,
            self.email,
            self.password
        )

        self.new_sensor_data = {
            "mac": self.sensorid,
            "lat": "4.12345678",
            "lon": "-74.12345678",
            "name": self.sensorname
        }

        self.new_point_data = [
            {
                "measurement": self.sensorname,
                "nameId": self.sensorname,
                "sensorId": self.sensorid,
                "fields": {
                "pm1": 0.0,
                "pm25": float(randint(0, self.maxpm25)),
                "pm10": 0.0,
                "hum": 0.0,
                "tmp": 0.0
                }
            }
        ]
        self.client.force_authenticate(user=self.user)

    def test_createsensor(self):
        url_sensor = reverse('sensors-list')
        res = self.client.get(url_sensor)
        sensor_count = len(res.data)

        res = self.client.post(url_sensor, self.new_sensor_data)
        self.assertEqual(res.status_code, 201)

        res = self.client.get(url_sensor)
        self.assertEqual(len(res.data), sensor_count + 1)
        data = res.data[-1]
        self.assertEqual(self.new_sensor_data['mac'], data['mac'])
        self.assertEqual(self.new_sensor_data['lat'], data['lat'])
        self.assertEqual(self.new_sensor_data['lon'], data['lon'])
        self.assertEqual(self.new_sensor_data['name'], data['name'])

    def test_save_and_retrieve_measure(self):
        url_save = reverse('save-measure')
        res = self.client.post(url_save, data=self.new_point_data, format='json')
        self.assertEqual(res.status_code, 201)

        url_get_latest = reverse('latest-measure')
        res = self.client.get(url_get_latest)
        self.assertEqual(res.status_code, 200)
        data = res.data[0]
        self.assertEqual(data['name'], self.sensorname)
        self.assertEqual(
            float(data['last_pm25']),
            self.new_point_data[0]['fields']['pm25']
        )

        # We should have added data recently
        ellapsed_seconds = (datetime.utcnow() - datetime.strptime(
            data['time'][:-4],
            '%Y-%m-%dT%H:%M:%S.%f')
        ).seconds
        self.assertEqual(ellapsed_seconds, 0)
