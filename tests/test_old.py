import unittest
from unittest.mock import MagicMock

from orbit import Orbit
from travel_option import TravelOption
from travel_option_provider import TravelOptionProvider, TravelOptionSelector
from vehicle import Vehicle, VehicleType


class TravelOptionProvidertests(unittest.TestCase):

    @staticmethod
    def create_travel_option(travel_time, vehicle_type, orbit_name):

        option = TravelOptionMock()
        option.get_travel_time = MagicMock(return_value=travel_time)
        option.get_vehicle = MagicMock(return_value=vehicle_type)
        option.get_orbit = MagicMock(return_value=orbit_name)
        return option

    def test_ss(self):
        options = [
            self.create_travel_option(travel_time=4, vehicle_type=VehicleType.BIKE, orbit_name="o1"),
            self.create_travel_option(travel_time=4, vehicle_type=VehicleType.CAR, orbit_name="o2"),
            self.create_travel_option(travel_time=4, vehicle_type=VehicleType.TUKTUK, orbit_name="o3"),
        ]
        option = TravelOptionSelector().select(options)
        assert option.get_vehicle() == VehicleType.BIKE


class TravelOptionMock:
    def get_travel_time(self):
        pass

    def get_vehicle(self):
        pass

    def get_orbit(self):
        pass



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