import unittest
from travel_option_provider import TravelOptionSelector
from vehicle import VehicleType


class TravelOptionSelectorTests(unittest.TestCase):

    def test_best_travel_option_is_based_vehicle_type_when_there_is_a_tie(self):
        tests = [
            (VehicleType.BIKE, [VehicleType.BIKE, VehicleType.CAR, VehicleType.TUKTUK]),
            (VehicleType.TUKTUK, [VehicleType.CAR, VehicleType.TUKTUK]),
            (VehicleType.CAR, [VehicleType.CAR]),
        ]
        for test in tests:
            with self.subTest(type=test[0]):
                options = list(map(lambda x: TravelOptionMock(4, x, "orbit"), test[1]))
                option = TravelOptionSelector().select(options)
                assert option.get_vehicle() == test[0]


class TravelOptionMock:
    def __init__(self, travel_time, vehicle_type, orbit_name):
        self.orbit_name = orbit_name
        self.vehicle_type = vehicle_type
        self.travel_time = travel_time

    def get_travel_time(self):
        return self.travel_time

    def get_vehicle(self):
        return self.vehicle_type

    def get_orbit(self):
        return self.orbit_name
