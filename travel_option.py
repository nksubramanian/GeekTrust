class TravelOption:
    def __init__(self, orbit, vehicle):
        self.__orbit = orbit
        self.__vehicle = vehicle
        self.__vehicle_type = vehicle.get_vehicle_type()
        self.__orbit_name = orbit.get_orbit_name()
        self.travel_time = self.__vehicle.compute_time_for_orbit(self.__orbit)

    def get_travel_time(self):
        return self.travel_time

    def get_vehicle(self):
        return self.__vehicle_type

    def get_orbit(self):
        return self.__orbit_name
