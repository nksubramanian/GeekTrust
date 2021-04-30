class TravelOption:
    def __init__(self, orbit, vehicle):
        self.orbit = orbit
        self.vehicle = vehicle

    def get_travel_time(self):
        return self.vehicle.compute_time_for_orbit(self.orbit)

    def get_vehicle(self):
        return self.vehicle.get_vehicle_type()

    def get_orbit(self):
        return self.orbit.get_orbit_name()
