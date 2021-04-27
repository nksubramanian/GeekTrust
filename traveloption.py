class TravelOption:
    def __init__(self, orbit, vehicle):
        self.orbit = orbit
        self.vehicle = vehicle
        self.vehicle_type = vehicle.vehicle_type

    def get_travel_time(self):
        speed = min(self.vehicle.speed, self.orbit.orbit_traffic_speed)
        time_to_cover_orbit = self.orbit.distance/speed
        time_to_cross_craters = self.orbit.no_of_craters * self.vehicle.crater_time / 60
        return time_to_cross_craters + time_to_cover_orbit

    def get_travel_details(self):
        return str(self.orbit.name) + " " + str(self.vehicle_type)
