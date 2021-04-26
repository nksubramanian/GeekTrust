from orbit import Orbit


class Weather:
    def __init__(self, name, crater_change, vehicle_type_allowed):
        self.name = name
        self.crater_change_percent = crater_change
        self.vehicle_type_allowed = vehicle_type_allowed

    def effect(self, orbit):
        no_of_craters = orbit.no_of_craters + self.crater_change_percent*orbit.no_of_craters/100
        return Orbit(orbit.name, orbit.road, no_of_craters, orbit.orbit_traffic_speed)

    def is_vehicle_allowed(self, vehicle):
        if vehicle.vehicle_type in self.vehicle_type_allowed:
            return True
        else:
            return False
