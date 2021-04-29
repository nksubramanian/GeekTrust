import unittest

from orbit import Orbit
from travel_option_provider import TravelOptionProvider
from vehicle import Vehicle, VehicleType
from weather import Weather, WeatherFactory


class VehicleTest(unittest.TestCase):

    def test_correct_type_of_vehile_is_created(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        assert vehicle.get_vehicle_type() == VehicleType.CAR


    def test_travel_time_is_computed_based_orbit(self):
        tests = [
            {
                "test_num": 1,
                "vehicle_type": VehicleType.CAR,
                "vehicle_speed": 10,
                "time_to_crater": 3,
                "orbit": Orbit("ORBIT1", 20, 10),
                "speed_limit": 45,
                "expected_time_taken": 2.5
            },
            {
                "test_num": 2,
                "vehicle_type": VehicleType.BIKE,
                "vehicle_speed": 12,
                "time_to_crater": 2,
                "orbit": Orbit("ORBIT1", 20, 30),
                "speed_limit": 10,
                "expected_time_taken": 3
            },
        ]
        for t in tests:
            with self.subTest(test_num=t["test_num"]):
                vehicle = Vehicle(t["vehicle_type"], t["vehicle_speed"], t["time_to_crater"])
                orbit = t["orbit"]
                orbit.set_orbit_traffic_speed(t["speed_limit"])
                time_taken = vehicle.compute_time_for_orbit(orbit)
                print(time_taken)
                assert t["expected_time_taken"] == time_taken





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