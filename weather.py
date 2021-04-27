class WeatherFactory:

    @staticmethod
    def create_weather(weather):
        if weather == "Sunny":
            return Weather("Sunny", -10, ["Car", "Bike", "TukTuk"])
        if weather == "Rainy":
            return Weather("Rainy", 20, ["Car", "TukTuk"])
        if weather == "Windy":
            return Weather("Windy", 0, ["Car", "Bike"])


class Weather:
    def __init__(self, name, crater_change_percentage, allowed_vehicles):
        self.name = name
        self.crater_change_percentage = crater_change_percentage
        self.allowed_vehicles = allowed_vehicles

    def adjust_crater(self, orbit):
        orbit.no_of_craters = orbit.no_of_craters + self.crater_change_percentage * orbit.no_of_craters / 100

