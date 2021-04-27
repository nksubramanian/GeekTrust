from orbit import Orbit, OrbitRepository
from weather import WeatherFactory
from vehicle import VehicleCreator
from traveloption import TravelOption


class Assistance:

    def get_fastest_vehicle_and_route(self, weather_string, traffic_speed_limits):

        orbits = OrbitRepository().get_orbits()
        self.__set_traffic_speed_limit(orbits, traffic_speed_limits)

        weather = WeatherFactory.create_weather(weather_string)

        allowed_vehicles = VehicleCreator.create_vehicles(weather.allowed_vehicles)
        weather_adjusted_orbits = weather.adjust_orbits(orbits)
        travel_options = list(map(TravelOption, orbits * len(allowed_vehicles),
                                  allowed_vehicles * len(weather_adjusted_orbits)))
        travel_options_time = list(map(TravelOption.get_travel_time, travel_options))
        fastest_option = travel_options[travel_options_time.index(min(travel_options_time))]
        return fastest_option.get_travel_details()

    def __set_traffic_speed_limit(self, orbits, traffic_speed_limits):
        for i in range(0, len(traffic_speed_limits)):
            orbits[i].set_orbit_traffic_speed(traffic_speed_limits[i])
