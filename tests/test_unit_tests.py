import unittest

from orbit import OrbitRepository, Orbit
from vehicle import VehicleCreator, Vehicle
from weather import Weather, WeatherFactory, VehicleType


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

    def test_weather_is_created_correctly_based_on_weather_string(self):
        tests =[["SUNNY", -10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK]],
                ["WINDY", 0, [VehicleType.CAR, VehicleType.BIKE]],
                ["RAINY", 20, [VehicleType.CAR, VehicleType.TUKTUK]]]

        for test in tests:
            weather = WeatherFactory.create_weather(test[0])
            assert set(test[2]) == set(weather.get_allowed_vehicles())

    def test_traffic_speed_limit_gets_added_correctly(self):
        orbits = OrbitRepository().get_orbits()
        assert orbits[0].orbit_traffic_speed is None
        assert orbits[1].orbit_traffic_speed is None
        orbits[0].set_orbit_traffic_speed(45)
        orbits[1].set_orbit_traffic_speed(54)
        assert orbits[0].orbit_traffic_speed == 45
        assert orbits[1].orbit_traffic_speed == 54


    def test_craters_of_orbit_are_modified_correctly_based_on_weather(self):
        orbit_test = Orbit("ORBIT1", 20, 10)
        weather = Weather(-10, [VehicleType.CAR, VehicleType.TUKTUK])
        assert orbit_test.no_of_craters == 10
        weather.adjust_crater(orbit_test)
        assert orbit_test.no_of_craters == 9








