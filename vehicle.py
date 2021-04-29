import enum


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TUKTUK = 3


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
        speed = min(self.speed, orbit.orbit_traffic_speed)
        time_to_cover_orbit = orbit.distance/speed
        time_to_cross_craters = orbit.no_of_craters * self.crater_time / 60
        return time_to_cross_craters + time_to_cover_orbit



