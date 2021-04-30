from weather import WeatherFactory
from vehicle import VehicleRepository, VehicleType
from travel_option import TravelOption
from travel_option_selector import TravelOptionSelector


class TravelOptionProvider:
    def __init__(self, orbit_repository):
        self.__orbit_repository = orbit_repository

    def get_travel_option(self, weather_string, traffic_speed_limits):
        orbits = self.__orbit_repository.get_orbits()
        weather = WeatherFactory.create_weather(weather_string)
        vehicles = VehicleRepository.get_vehicles(weather.get_allowed_vehicles())

        self.__set_traffic_speed_limit(orbits, traffic_speed_limits)
        self.__adjust_crater_in_orbits(orbits, weather)
        travel_options = self.__get_travel_options(orbits, vehicles)

        return TravelOptionSelector().select(travel_options)

    def __get_travel_options(self, orbits, vehicles):
        travel_options = []
        for orbit in orbits:
            for vehicle in vehicles:
                travel_options.append(TravelOption(orbit, vehicle))
        return travel_options

    def __adjust_crater_in_orbits(self, orbits, weather):
        for orbit in orbits:
            weather.adjust_crater(orbit)

    def __set_traffic_speed_limit(self, orbits, traffic_speed_limits):
        for i in range(0, len(traffic_speed_limits)):
            orbits[i].set_orbit_traffic_speed(traffic_speed_limits[i])
