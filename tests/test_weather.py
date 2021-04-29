import unittest

from orbit import Orbit
from vehicle import VehicleType
from weather import Weather, WeatherFactory


class WeatherTest(unittest.TestCase):
    def test_weather_is_correctly_created(self):
        weather = Weather(10, [VehicleType.TUKTUK, VehicleType.BIKE])
        assert weather.get_crater_change_percentage() == 10
        assert weather.get_allowed_vehicles() == [VehicleType.TUKTUK, VehicleType.BIKE]

    def test_weather_factory_creates_the_weather_correctly(self):
        tests = [["SUNNY", -10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK]],
                 ["WINDY", 0, [VehicleType.CAR, VehicleType.BIKE]],
                 ["RAINY", 20, [VehicleType.CAR, VehicleType.TUKTUK]]]
        for test in tests:
            with self.subTest(test=test[0]):
                weather = WeatherFactory.create_weather(test[0])
                assert set(test[2]) == set(weather.get_allowed_vehicles())
                assert weather.get_crater_change_percentage() == test[1]

    def test_weather_alters_the_orbit_correctly(self):
        orbit_test = Orbit("ORBIT1", 20, 10)
        weather = Weather(-10, [VehicleType.BIKE, VehicleType.TUKTUK])
        weather.adjust_crater(orbit_test)
        assert orbit_test.no_of_craters == 9