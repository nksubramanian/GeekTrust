import unittest

from orbit import Orbit
from vehicle import Vehicle, VehicleType


class VehicleTest(unittest.TestCase):

    def test_correct_type_of_vehile_is_created(self):
        vehicle = Vehicle(VehicleType.CAR, 10, 60)
        assert vehicle.get_vehicle_type() == VehicleType.CAR

    def test_travel_time_is_computed_based_orbit(self):
        tests = [
            {
                "test_num": 1,
                "vehicle_type": VehicleType.CAR,
                "vehicle_speed": 10,
                "time_to_crater": 3,
                "orbit": Orbit("ORBIT1", 20, 10),
                "speed_limit": 45,
                "expected_time_taken": 2.5
            },
            {
                "test_num": 2,
                "vehicle_type": VehicleType.BIKE,
                "vehicle_speed": 12,
                "time_to_crater": 2,
                "orbit": Orbit("ORBIT1", 20, 30),
                "speed_limit": 10,
                "expected_time_taken": 3
            },
        ]
        for t in tests:
            with self.subTest(test_num=t["test_num"]):
                vehicle = Vehicle(t["vehicle_type"], t["vehicle_speed"], t["time_to_crater"])
                orbit = t["orbit"]
                orbit.set_orbit_traffic_speed(t["speed_limit"])
                time_taken = vehicle.compute_time_for_orbit(orbit)
                print(time_taken)
                assert t["expected_time_taken"] == time_taken

