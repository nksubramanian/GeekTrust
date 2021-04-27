class Orbit:
    def __init__(self, name, distance, no_of_craters):
        self.name = name
        self.distance = distance
        self.no_of_craters = no_of_craters
        self.orbit_traffic_speed = None

    def set_orbit_traffic_speed(self, orbit_traffic_speed):
        self.orbit_traffic_speed = orbit_traffic_speed

