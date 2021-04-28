import unittest
from assistance import TravelOptionProvider
from weather import VehicleType


class VehicleTest(unittest.TestCase):
    def test_when_vehicle_is_bike_then_create_vehicle_returns_bike(self):
        tests = [["RAINY", [40, 25], (VehicleType.CAR, "ORBIT2")],
                 ["RAINY", [12, 12], (VehicleType.TUKTUK, "ORBIT2")],
                 ["SUNNY", [50, 50], (VehicleType.CAR, "ORBIT2")],
                 ["SUNNY", [5, 50],  (VehicleType.CAR, "ORBIT2")],
                 ["SUNNY", [5, 50], (VehicleType.CAR, "ORBIT2")]]

        for test in tests:
            travel_option = TravelOptionProvider().get_best_travel_option(test[0], test[1])
            assert (travel_option.vehicle_type, travel_option.orbit_name ) == test[2]



