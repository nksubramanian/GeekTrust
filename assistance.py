from orbit import Orbit, OrbitRepository
from weather import WeatherFactory
from vehicle import VehicleCreator
from traveloption import TravelOption


class Assistance:

    def get_best_travel_option(self, weather_string, traffic_speed_limits):

        orbits = OrbitRepository().get_orbits()
        self.__set_traffic_speed_limit(orbits, traffic_speed_limits)
        weather = WeatherFactory.create_weather(weather_string)
        vehicles = VehicleCreator.create_vehicles(weather.allowed_vehicles)
        for orbit in orbits:
            weather.adjust_crater(orbit)
        travel_options = []
        for orbit in orbits:
            for vehicle in vehicles:
                travel_options.append(TravelOption(orbit, vehicle))
        travel_times = list(map(lambda x: x.get_travel_time(), travel_options))
        fastest_travel_time = min(travel_times)
        fastest_routes = filter(lambda x: travel_options.get_travel_time() == fastest_travel_time,
                                travel_options)
        return fastest_routes

    def __set_traffic_speed_limit(self, orbits, traffic_speed_limits):
        for i in range(0, len(traffic_speed_limits)):
            orbits[i].set_orbit_traffic_speed(traffic_speed_limits[i])
