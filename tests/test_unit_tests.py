import unittest

from orbit import OrbitRepository
from vehicle import VehicleCreator, Vehicle
from weather import Weather, WeatherFactory, VehicleType, WeatherType


class VehicleTest(unittest.TestCase):
    def test_when_vehicle_is_bike_then_create_vehicle_returns_bike(self):
        vehicle = VehicleCreator.create_vehicle("Bike")
        assert vehicle.vehicle_type == "Bike"
        assert vehicle.speed == 10
        assert vehicle.crater_time == 2
        assert Vehicle("Bike", 10, 2).__eq__(vehicle) == True


    def test_get_orbits_return_orbits_with_specifications_as_mentioned_in_question(self):
        orbits = OrbitRepository().get_orbits()
        values = [[0, ("ORBIT1", 18, 20)], [1, ("ORBIT2", 20, 10)]]
        for value in values:
            assert (orbits[value[0]].name, orbits[value[0]].distance, orbits[value[0]].no_of_craters) == value[1]

    def test_create_weather_creates_correct_weather_objects_with_mentioned_specifications(self):
        values = [["SUNNY", Weather(WeatherType.SUNNY, -10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK])],
                  ["WINDY", Weather(WeatherType.WINDY, -10, [VehicleType.CAR, VehicleType.BIKE])],
                  ["RAINY", Weather(WeatherType.RAINY, -10, [VehicleType.CAR, VehicleType.TUKTUK])]]

        for value in values:
            weather = WeatherFactory.create_weather(values[0])
            assert weather.__eq__(value[1])



