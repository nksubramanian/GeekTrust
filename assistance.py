from orbit import Orbit, OrbitRepository
from weather import WeatherFactory
from vehicle import VehicleCreator
from traveloption import TravelOption


class Assistance:

    def get_fastest_vehicle_and_route(self, weather, orbit1_travel_time, orbit2_travel_time):

        orbitRepo = OrbitRepository()
        orbits = orbitRepo.get_orbits()

        self.orbit1 = orbits[0]
        self.orbit2 = orbits[1]

        self.orbit1.set_orbit_traffic_speed(orbit1_travel_time)
        self.orbit2.set_orbit_traffic_speed(orbit2_travel_time)
        self.user_weather = WeatherFactory.create_weather(weather)





        allowed_vehicles = VehicleCreator.create_vehicles(self.user_weather.allowed_vehicles)
        orbits = [self.orbit1, self.orbit2]
        weather_adjusted_orbits = self.user_weather.adjust_orbits(orbits)
        travel_options = list(map(TravelOption, orbits * len(allowed_vehicles),
                                  allowed_vehicles * len(weather_adjusted_orbits)))
        travel_options_time = list(map(TravelOption.get_travel_time, travel_options))
        fastest_option = travel_options[travel_options_time.index(min(travel_options_time))]
        return fastest_option.get_travel_details()
