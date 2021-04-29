import unittest

from orbit import OrbitRepository, Orbit
from vehicle import VehicleCreator, Vehicle
from weather import Weather, WeatherFactory, VehicleType
from travel_option import TravelOption

class OrbitTest(unittest.TestCase):

    def test_get_orbits_return_orbits_with_specifications_as_mentioned_in_question(self):
        orbit_parameters = [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]
        orbit_repository = OrbitRepository(orbit_parameters)
        orbits = orbit_repository.get_orbits()
        values = [[0, ("ORBIT1", 18, 20)], [1, ("ORBIT2", 20, 10)]]
        for value in values:
            assert (orbits[value[0]].get_orbit_name(), orbits[value[0]].distance, orbits[value[0]].no_of_craters) == value[1]

    def test_traffic_speed_limit_gets_added_correctly(self):
        orbit_parameters = [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]
        orbit_repository = OrbitRepository(orbit_parameters)
        orbits = orbit_repository.get_orbits()
        assert orbits[0].orbit_traffic_speed is None
        assert orbits[1].orbit_traffic_speed is None
        orbits[0].set_orbit_traffic_speed(45)
        orbits[1].set_orbit_traffic_speed(54)
        assert orbits[0].orbit_traffic_speed == 45
        assert orbits[1].orbit_traffic_speed == 54




class VehicleTest(unittest.TestCase):

    def test_vehicle_are_being_created_based_on_specifications(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        assert vehicle.get_vehicle_type() == VehicleType.CAR


    def test_minimum_of_orbit_traffic_speed_and_vehicle_speed_is_used_to_compute_time_for_orbits(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        orbit = Orbit("ORBIT1", 20, 10)
        orbit.set_orbit_traffic_speed(45)
        assert vehicle.compute_time_for_orbit(orbit) == 12
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        orbit = Orbit("ORBIT1", 20, 10)
        orbit.set_orbit_traffic_speed(5)
        assert vehicle.compute_time_for_orbit(orbit) == 14

    class WeatherTest(unittest.TestCase):
        def test_weather_can_be_created_as_specified_attributed(self):
            weather = Weather(10, [VehicleType.CAR, VehicleType.BIKE])



        def test_weather_is_created_correctly_based_on_weather_string(self):
            tests = [["SUNNY", -10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK]],
                     ["WINDY", 0, [VehicleType.CAR, VehicleType.BIKE]],
                     ["RAINY", 20, [VehicleType.CAR, VehicleType.TUKTUK]]]
            for test in tests:
                weather = WeatherFactory.create_weather(test[0])
                assert set(test[2]) == set(weather.get_allowed_vehicles())
                assert weather.get_crater_change_percentage() == test[1]


        def test_craters_of_orbit_are_modified_correctly_based_on_weather(self):
            orbit_test = Orbit("ORBIT1", 20, 10)
            weather = Weather(-10, [VehicleType.CAR, VehicleType.TUKTUK])
            assert orbit_test.no_of_craters == 10
            weather.adjust_crater(orbit_test)
            assert orbit_test.no_of_craters == 9
















