class TravelOption:
    def __init__(self, orbit, vehicle):
        self.__orbit = orbit
        self.__vehicle = vehicle

    def get_travel_time(self):
        return self.__vehicle.compute_time_for_orbit(self.__orbit)

    def get_vehicle(self):
        return self.__vehicle.get_vehicle_type()

    def get_orbit(self):
        return self.__orbit.get_orbit_name()
