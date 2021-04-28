class Orbit:
    def __init__(self, name, distance, no_of_craters):
        self.name = name
        self.distance = distance
        self.no_of_craters = no_of_craters
        self.orbit_traffic_speed = None

    def set_orbit_traffic_speed(self, orbit_traffic_speed):
        self.orbit_traffic_speed = orbit_traffic_speed


class OrbitRepository:
    # read this from a config file
    def get_orbits(self):
        from configparser import ConfigParser
        config = ConfigParser()
        config.read('F:\\GeekTrust\\config.ini')
        orbit1_name = config["ORBIT1"]["name"]
        orbit1_distance = int(config["ORBIT1"]["distance"])
        orbit1_no_of_craters= int(config["ORBIT1"]["no_of_craters"])
        orbit2_name = config["ORBIT2"]["name"]
        orbit2_distance = int(config["ORBIT2"]["distance"])
        orbit2_no_of_craters = int(config["ORBIT2"]["no_of_craters"])
        return Orbit(orbit1_name, orbit1_distance, orbit1_no_of_craters), Orbit(orbit2_name, orbit2_distance, orbit2_no_of_craters)


