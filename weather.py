import enum


class VehicleType(enum.Enum):
    Car = 1
    Bike = 2
    TukTuk = 3


class WeatherType(enum.Enum):
    SUNNY = 1
    RAINY = 2
    WINDY = 3


class WeatherFactory:

    @staticmethod
    def create_weather(weather):
        if weather == "SUNNY":
            return Weather(WeatherType.SUNNY, -10, [VehicleType.Car, VehicleType.Bike, VehicleType.TukTuk])
        if weather == "RAINY":
            return Weather(WeatherType.RAINY, 20, [VehicleType.Car, VehicleType.TukTuk])
        if weather == "WINDY":
            return Weather(WeatherType.WINDY, 0, [VehicleType.Car, VehicleType.Bike])


class Weather:
    def __init__(self, name, crater_change_percentage, allowed_vehicles):
        self.__name = name
        self.__crater_change_percentage = crater_change_percentage
        self.__allowed_vehicles = allowed_vehicles

    def adjust_crater(self, orbit):
        orbit.no_of_craters = orbit.no_of_craters + self.__crater_change_percentage * orbit.no_of_craters / 100

    def get_allowed_vehicles(self):
        return self.__allowed_vehicles
