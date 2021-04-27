from orbit import Orbit, OrbitRepository
from weather import WeatherFactory
from vehicle import VehicleCreator
from traveloption import TravelOption


class Assistance:

    def get_fastest_vehicle_and_route(self, weather_string, traffic_speed_limits):

        orbit_repository = OrbitRepository()
        orbits = orbit_repository.get_orbits()

        orbit1 = orbits[0]
        orbit2 = orbits[1]

        orbit1.set_orbit_traffic_speed(traffic_speed_limits[0])
        orbit2.set_orbit_traffic_speed(traffic_speed_limits[1])

        weather = WeatherFactory.create_weather(weather_string)

        allowed_vehicles = VehicleCreator.create_vehicles(weather.allowed_vehicles)
        orbits = [orbit1, orbit2]
        weather_adjusted_orbits = weather.adjust_orbits(orbits)
        travel_options = list(map(TravelOption, orbits * len(allowed_vehicles),
                                  allowed_vehicles * len(weather_adjusted_orbits)))
        travel_options_time = list(map(TravelOption.get_travel_time, travel_options))
        fastest_option = travel_options[travel_options_time.index(min(travel_options_time))]
        return fastest_option.get_travel_details()
