import unittest
from vehicle import VehicleCreator, Vehicle
import copy


class VehicleTest(unittest.TestCase):
    def test_when_vehicle_is_bike_then_create_vehicle_returns_bike(self):
        vehicle = VehicleCreator.create_vehicle("Bike")
        assert vehicle.vehicle_type == "Bike"
        assert vehicle.speed == 10
        assert vehicle.crater_time == 2
        assert Vehicle("Bike", 10, 2).__eq__(vehicle) == True


        # assert vehicle == Vehicle("Bike", 10, 2)






if __name__ == "__main__":
    unittest.main()