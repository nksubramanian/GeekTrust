class Orbit:
    def __init__(self, name, distance, no_of_craters):
        self.__name = name
        self.__distance = distance
        self.no_of_craters = no_of_craters
        self.orbit_traffic_speed = None

    def get_distance(self):
        return self.__distance

    def set_orbit_traffic_speed(self, orbit_traffic_speed):
        self.orbit_traffic_speed = orbit_traffic_speed

    def get_orbit_name(self):
        return self.__name

    #get crater
    #get distance
    #get_traffic_speed_limit



class OrbitRepository:
    def __init__(self, orbits_parameters):
        self.orbits_parameters = orbits_parameters

    def get_orbits(self):
        orbit_repository = []
        for orbit_parameters in self.orbits_parameters:
            orbit_repository.append(Orbit(orbit_parameters[0], orbit_parameters[1], orbit_parameters[2]))
        return orbit_repository


