from orbit import Orbit, OrbitRepository
from weather import WeatherFactory, VehicleType
from vehicle import VehicleCreator
from travel_option import TravelOption


class TravelOptionProvider:
    def __init__(self, orbit_repository):
        self.orbit_repository = orbit_repository

    def get_best_travel_option(self, weather_string, traffic_speed_limits):
        orbits = self.orbit_repository.get_orbits()
        self.__set_traffic_speed_limit(orbits, traffic_speed_limits)
        weather = WeatherFactory.create_weather(weather_string)
        vehicles = VehicleCreator.create_vehicles(weather.get_allowed_vehicles())
        self.adjust_crater_in_orbits(orbits, weather)
        travel_options = self.get_travel_options(orbits, vehicles)
        travel_options = self.get_fastest_travel_options(travel_options)
        return self.get_best_travel_option_based_on_vehicle(travel_options)

    def get_best_travel_option_based_on_vehicle(self, travel_options):
        for travel_option in travel_options:
            self.rank_travel_options_on_vehicle(travel_option)

        minimum_rank = min(map(lambda x: x.rank, travel_options))
        best_ranked_travel_options = list(filter(lambda x: x.rank == minimum_rank, travel_options))
        return best_ranked_travel_options[0]

    def rank_travel_options_on_vehicle(self, travel_option):
        ranking = {
            VehicleType.BIKE: 1,
            VehicleType.TUKTUK: 2,
            VehicleType.CAR: 3
        }
        rank = ranking[travel_option.vehicle_type]
        travel_option.rank = rank


    def get_fastest_travel_options(self, travel_options):
        travel_times = list(map(lambda x: x.get_travel_time(), travel_options))
        fastest_travel_time = min(travel_times)
        fastest_routes = list(filter(lambda x: x.get_travel_time() == fastest_travel_time,
                                travel_options))
        return fastest_routes

    def get_travel_options(self, orbits, vehicles):
        travel_options = []
        for orbit in orbits:
            for vehicle in vehicles:
                travel_options.append(TravelOption(orbit, vehicle))
        return travel_options

    def adjust_crater_in_orbits(self, orbits, weather):
        for orbit in orbits:
            weather.adjust_crater(orbit)

    def __set_traffic_speed_limit(self, orbits, traffic_speed_limits):
        for i in range(0, len(traffic_speed_limits)):
            orbits[i].set_orbit_traffic_speed(traffic_speed_limits[i])
