import unittest
from travel_option_provider import TravelOptionProvider
from orbit import OrbitRepository
from weather import VehicleType


class VehicleTest(unittest.TestCase):
    def test_when_weather_and_traffic_is_given_then_output_orbit_and_output_vehicle_is_correct(self):
        tests = [["RAINY", [40, 25], (VehicleType.CAR, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["RAINY", [12, 12], (VehicleType.TUKTUK, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [50, 50], (VehicleType.CAR, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [5, 50],  (VehicleType.CAR, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [50, 5], (VehicleType.TUKTUK, "ORBIT1"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["RAINY", [50, 50], (VehicleType.CAR, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [12, 10], (VehicleType.TUKTUK, "ORBIT1"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["WINDY", [14, 20], (VehicleType.CAR, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["RAINY", [8, 15], (VehicleType.TUKTUK, "ORBIT2"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [1, 1], (VehicleType.TUKTUK, "ORBIT1"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["SUNNY", [12, 12], (VehicleType.TUKTUK, "ORBIT1"), [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]],
                 ["WINDY", [30, 30], (VehicleType.BIKE, "ORBIT1"), [["ORBIT1", 20, 60], ["ORBIT2", 200, 10]]]]

        for test in tests:
            with self.subTest(test=test):
                orbit_parameters = test[3]
                orbit_repository = OrbitRepository(orbit_parameters)
                travel_option = TravelOptionProvider(orbit_repository).get_travel_option(test[0], test[1])
                assert (travel_option.get_vehicle(), travel_option.get_orbit()) == test[2]
