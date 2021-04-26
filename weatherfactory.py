from weather import Weather


class WeatherFactory:

    @staticmethod
    def get_weather(weather):
        if weather == "Sunny":
            return Weather("Sunny", -10, ["Car", "Bike", "TukTuk"])
        if weather == "Rainy":
            return Weather("Rainy", -10, ["Car", "TukTuk"])
        if weather == "Windy":
            return Weather("Windy", -10, ["Car", "Bike"])
