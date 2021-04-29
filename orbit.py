class Orbit:
    def __init__(self, name, distance, no_of_craters):
        self.__name = name
        self.distance = distance
        self.no_of_craters = no_of_craters
        self.orbit_traffic_speed = None

    def set_orbit_traffic_speed(self, orbit_traffic_speed):
        self.orbit_traffic_speed = orbit_traffic_speed

    def get_orbit_name(self):
        return self.__name



class OrbitRepository:
    def __init__(self, orbit_parameters):
        self.orbit_parameters = orbit_parameters

    def get_orbits(self):
        return [Orbit(self.orbit_parameters[0][0], self.orbit_parameters[0][1], self.orbit_parameters[0][2]),
                Orbit(self.orbit_parameters[1][0], self.orbit_parameters[1][1], self.orbit_parameters[1][2])]
