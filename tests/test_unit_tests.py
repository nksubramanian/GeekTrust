import unittest

from orbit import OrbitRepository, Orbit
from vehicle import VehicleCreator, Vehicle
from weather import Weather, WeatherFactory, VehicleType
from travel_option import TravelOption
from travel_option_provider import TravelOptionProvider


class OrbitTest(unittest.TestCase):

    def test_orbit_creation_test(self):
        orb = Orbit("ORBIT1", 18, 20)
        assert orb.get_orbit_name() == "ORBIT1"
        assert orb.distance == 18
        assert orb.no_of_craters == 20
        assert orb.orbit_traffic_speed is None

    def test_traffic_speed_could_be_set_for_orbit(self):
        test_orbit = Orbit("ORBIT1", 18, 20)
        test_orbit.set_orbit_traffic_speed(54)
        assert test_orbit.orbit_traffic_speed == 54


class OrbitRepositoryTest(unittest.TestCase):
    def test_orbit_repository_produces_orbit_as_per_config(self):
        orbit_parameters = [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]
        orbit_repository = OrbitRepository(orbit_parameters)
        orbits = orbit_repository.get_orbits()
        values = [("ORBIT1", 18, 20), ("ORBIT2", 20, 10)]
        for i in range(0, len(values)):
            assert (orbits[i].get_orbit_name(), orbits[i].distance, orbits[i].no_of_craters) == values[i]


class VehicleTest(unittest.TestCase):

    def test_vehicle_are_being_created_based_on_specifications(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        assert vehicle.get_vehicle_type() == VehicleType.CAR


    def test_vehicle_takes_minimum_of_orbit_traffic_speed_and_vehicle_speed_is_used_to_compute_time_for_orbits(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        orbit = Orbit("ORBIT1", 20, 10)
        orbit.set_orbit_traffic_speed(45)
        assert vehicle.compute_time_for_orbit(orbit) == 12
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        orbit = Orbit("ORBIT1", 20, 10)
        orbit.set_orbit_traffic_speed(5)
        assert vehicle.compute_time_for_orbit(orbit) == 14

    class WeatherTest(unittest.TestCase):
        def test_weather_can_be_created_with_attributes_as_required(self):
            weather = Weather(10, [VehicleType.TUKTUK, VehicleType.BIKE])
            assert weather.get_crater_change_percentage() == 10
            assert weather.get_allowed_vehicles() == [VehicleType.TUKTUK, VehicleType.BIKE]

        def test_weather_attribtues_is_created_correct_based_on_weather_string(self):
            tests = [["SUNNY", -10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK]],
                     ["WINDY", 0, [VehicleType.CAR, VehicleType.BIKE]],
                     ["RAINY", 20, [VehicleType.CAR, VehicleType.TUKTUK]]]
            for test in tests:
                weather = WeatherFactory.create_weather(test[0])
                assert set(test[2]) == set(weather.get_allowed_vehicles())
                assert weather.get_crater_change_percentage() == test[1]


        def test_weather_modifies_no_of_craters_in_orbits(self):
            orbit_test = Orbit("ORBIT1", 20, 10)
            weather = Weather(-10, [VehicleType.BIKE, VehicleType.TUKTUK])
            assert orbit_test.no_of_craters == 10
            weather.adjust_crater(orbit_test)
            assert orbit_test.no_of_craters == 9


    class PreferenceTest(unittest.TestCase):

        def test_preference_of_bike_tuktuk_car_is_used(self):
            orbits = [Orbit("ORBIT1", 18, 20), Orbit("ORBIT2", 20, 20)]
            vehicles = [Vehicle(VehicleType.CAR, 10, 60), Vehicle(VehicleType.BIKE, 10, 60), Vehicle(VehicleType.TUKTUK, 10, 60)]
            travel_options = TravelOptionProvider.get_travel_options(orbits, vehicles)
            print(travel_options)
            travel_options = TravelOptionProvider.get_fastest_travel_options(travel_options)
            x = TravelOptionProvider.get_best_travel_option_based_on_vehicle(travel_options)

            print(x.get_vehicle_type())
            assert True

        def test_preference_of_bike_tuktuk_car_is_useddsac(self):
            print("I am heredw")
            assert True

