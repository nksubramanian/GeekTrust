import enum


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TUKTUK = 3


class VehicleRepository:
    @staticmethod
    def get_vehicles(vehicle_names):
        x = map(VehicleRepository.create_vehicle, vehicle_names)
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
        self.__vehicle_type = vehicle_type
        self.__speed = speed
        self.__crater_time = crater_time

    def get_vehicle_type(self):
        return self.__vehicle_type

    def compute_time_for_orbit(self, orbit):
        speed = min(self.__speed, orbit.orbit_traffic_speed)
        time_to_cover_orbit = orbit.get_distance() / speed
        time_to_cross_craters = orbit.get_num_craters() * self.__crater_time / 60
        return time_to_cross_craters + time_to_cover_orbit



