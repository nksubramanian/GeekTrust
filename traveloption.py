class TravelOption:
    def __init__(self, orbit, vehicle):
        self.orbit = orbit
        self.vehicle = vehicle

    def get_travel_time(self):
        return (self.orbit.distance/self.vehicle.speed) + self.orbit.no_of_craters*self.vehicle.crater_time/60

    def get_travel_details(self):
        return str(self.orbit.name) + " " + str(self.vehicle.vehicle_type)
