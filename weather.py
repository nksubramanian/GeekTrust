from orbit import Orbit


class Weather:
    def __init__(self, name, crater_change, vehicle_type_allowed):
        self.name = name
        self.crater_change_percent = crater_change
        self.vehicle_type_allowed = vehicle_type_allowed

    def effect_on_orbit(self, orbit):
        no_of_craters = orbit.no_of_craters + self.crater_change_percent*orbit.no_of_craters/100
        return Orbit(orbit.name, orbit.road, no_of_craters, orbit.orbit_traffic_speed)

    def effect_on_orbits(self, orbits):
        modified_orbits = []
        for orbit in orbits:
            modified_orbits.append(self.effect_on_orbit(orbit))
        return modified_orbits
