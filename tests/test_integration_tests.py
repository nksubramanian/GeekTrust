import unittest
from assistance import TravelOptionProvider
from weather import VehicleType


class VehicleTest(unittest.TestCase):
    def test_when_vehicle_is_bike_then_create_vehicle_returns_bike(self):
        travel_option = TravelOptionProvider().get_best_travel_option("RAINY", [40, 25])
        assert travel_option.vehicle_type == VehicleType.CAR
        assert travel_option.orbit_name == "ORBIT2"
