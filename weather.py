from vehicle import VehicleType


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
        orbit.alter_number_of_craters(self.__crater_change_percentage)

    def get_allowed_vehicles(self):
        return self.__allowed_vehicles

    def get_crater_change_percentage(self):
        return self.__crater_change_percentage
