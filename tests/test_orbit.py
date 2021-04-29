import unittest

from orbit import Orbit


class OrbitTest(unittest.TestCase):

    def test_orbit_creation_test(self):
        orb = Orbit("ORBIT1", 18, 20)
        assert orb.get_orbit_name() == "ORBIT1"
        assert orb.get_distance() == 18
        assert orb.get_num_craters() == 20
        assert orb.orbit_traffic_speed is None

    def test_traffic_speed_could_be_set_for_orbit(self):
        test_orbit = Orbit("ORBIT1", 18, 20)
        test_orbit.set_orbit_traffic_speed(54)
        assert test_orbit.orbit_traffic_speed == 54

    def test_number_of_craters_could_altered(self):
        test_orbit = Orbit("ORBIT1", 18, 20)
        test_orbit.alter_number_of_craters(10)
        assert test_orbit.get_num_craters() == 22
