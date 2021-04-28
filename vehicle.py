from weather import VehicleType


class VehicleCreator:

    @staticmethod
    def create_vehicles(vehicle_names):
        x = map(VehicleCreator.create_vehicle, vehicle_names)
        return list(x)

    @staticmethod
    def create_vehicle(vehicle_name):
        if vehicle_name == VehicleType.BIKE:
            return Vehicle(VehicleType.BIKE, 10, 2)
        if vehicle_name == VehicleType.TUKTUK:
            return Vehicle(VehicleType.TUKTUK, 12, 1)
        if vehicle_name == VehicleType.CAR:
            return Vehicle(VehicleType.CAR, 20, 3)


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


