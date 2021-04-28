import enum


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TUKTUK = 3


class WeatherFactory:

    @staticmethod
    def create_weather(weather):
        if weather == "SUNNY":
            return Weather(-10, [VehicleType.CAR, VehicleType.BIKE, VehicleType.TUKTUK])
        if weather == "RAINY":
            return Weather(20, [VehicleType.CAR, VehicleType.TUKTUK])
        if weather == "WINDY":
            return Weather(0, [VehicleType.CAR, VehicleType.BIKE])


class Weather:
    def __init__(self, crater_change_percentage, allowed_vehicles):
        self.__crater_change_percentage = crater_change_percentage
        self.__allowed_vehicles = allowed_vehicles

    def adjust_crater(self, orbit):
        orbit.no_of_craters = orbit.no_of_craters + self.__crater_change_percentage * orbit.no_of_craters / 100

    def get_allowed_vehicles(self):
        return self.__allowed_vehicles



