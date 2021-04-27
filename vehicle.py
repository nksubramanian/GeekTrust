class VehicleCreator:

    @staticmethod
    def create_vehicles(allowed_vehicles):
        x = map(VehicleCreator.create_vehicle, allowed_vehicles)
        return list(x)

    @staticmethod
    def create_vehicle(vehicle):
        if vehicle == "Bike":
            return Vehicle("Bike", 10, 2)
        if vehicle == "TukTuk":
            return Vehicle("TukTuk", 12, 1)
        if vehicle == "Car":
            return Vehicle("Car", 20, 3)


class Vehicle:
    def __init__(self, vehicle_type, speed, crater_time):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.crater_time = crater_time

    def compute_time_for_orbit(self, orbit):
        time = (orbit.distance/self.speed) + orbit.no_of_craters*self.crater_time/60
        return time

    def compute_time_for_orbits(self, orbits):
        time = []
        for orbit in orbits:
            time.append(self.compute_time_for_orbit(orbit))
        return time

    def __eq__(self, other):
        return (self.vehicle_type, self.speed, self.crater_time) == (other.vehicle_type, other.speed, other.crater_time)


