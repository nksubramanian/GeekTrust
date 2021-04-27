import unittest
from assistance import TravelOptionProvider
import copy


class VehicleTest(unittest.TestCase):
    def test_when_vehicle_is_bike_then_create_vehicle_returns_bike(self):
        #Correct the spelling of weather
        #correct the spelling of vehicle
        travel_option = TravelOptionProvider().get_best_travel_option("Rainy", [40, 25])
        assert travel_option.vehicle_type == "Car"
        assert travel_option.orbit_name == "ORBIT2"
