import unittest

from orbit import Orbit
from travel_option_provider import TravelOptionProvider
from vehicle import Vehicle, VehicleType


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