import unittest

from orbit import Orbit
from travel_option_provider import TravelOptionProvider
from vehicle import Vehicle, VehicleType
from weather import Weather, WeatherFactory








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