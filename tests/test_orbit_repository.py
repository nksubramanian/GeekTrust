import unittest

from orbit import OrbitRepository


class OrbitRepositoryTest(unittest.TestCase):
    def test_orbit_repository_produces_orbit_as_per_config(self):
        config = [["ORBIT1", 18, 20], ["ORBIT2", 20, 10]]
        repo = OrbitRepository(config)
        orbits = repo.get_orbits()
        for i in range(0, len(config)):
            assert orbits[i].get_orbit_name() == config[i][0]
            assert orbits[i].get_distance() == config[i][1]
            assert orbits[i].get_num_craters() == config[i][2]