import unittest
from unittest import mock
from travel_option_selector import TravelOptionSelector
from vehicle import VehicleType
from travel_option import TravelOption


class TravelOptionSelectorTests(unittest.TestCase):

    def test_best_travel_option_is_based_time_of_travel_second(self):
        tests = [
            (4, [8, 5, 4]),
            (3, [3, 6, 7]),
        ]
        for test in tests:
            with self.subTest(test=test):
                options = list(map(lambda x: self.travel_options_creator(x, VehicleType.CAR), test[1]))
                option = TravelOptionSelector().select(options)
                assert option.get_travel_time() == test[0]


    def test_best_travel_option_is_based_time_of_travel_third(self):
        tests = [
            (VehicleType.BIKE, [VehicleType.BIKE, VehicleType.CAR, VehicleType.TUKTUK]),
            (VehicleType.TUKTUK, [VehicleType.CAR, VehicleType.TUKTUK]),
            (VehicleType.CAR, [VehicleType.CAR]),
        ]
        for test in tests:
            with self.subTest(testcase=test[0]):
                options = list(map(lambda x: self.travel_options_creator(3, x), test[1]))
                option = TravelOptionSelector().select(options)
                assert option.get_vehicle() == test[0]

    def travel_options_creator(self, speed, vehicle_type):
        x = TravelOption(None, None)
        x.get_vehicle = mock.Mock(return_value=vehicle_type)
        x.get_travel_time = mock.Mock(return_value=speed)
        return x