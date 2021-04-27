from orbit import Orbit
from weather import WeatherFactory
from vehicle import VehicleCreator
from traveloption import TravelOption

if __name__ == '__main__':
    orbit1 = Orbit("ORBIT1", 18, 20)
    orbit2 = Orbit("ORBIT2", 20, 10)
    orbit1.set_orbit_traffic_speed(89)
    orbit2.set_orbit_traffic_speed(96)
    user_weather = WeatherFactory.create_weather("Sunny")
    allowed_vehicles = VehicleCreator.create_vehicles(user_weather.allowed_vehicles)
    orbits = [orbit1, orbit2]
    weather_adjusted_orbits = user_weather.adjust_orbits(orbits)
    travel_options = list(map(TravelOption, orbits * len(allowed_vehicles),
                              allowed_vehicles * len(weather_adjusted_orbits)))
    travel_options_time = list(map(TravelOption.get_travel_time, travel_options))
    fastest_option = travel_options[travel_options_time.index(min(travel_options_time))]
    print(fastest_option.get_travel_details())









