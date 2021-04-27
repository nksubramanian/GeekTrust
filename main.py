from orbit import Orbit
from weather import WeatherFactory
from vehicle import VehicleFactory
from decisionmaker import DecisionMaker

if __name__ == '__main__':
    ORBIT1 = Orbit("ORBIT1", 18, 20, 89)
    ORBIT2 = Orbit("ORBIT2", 20, 10, 95)
    user_weather = WeatherFactory.create_weather("Windy")
    vehicles_allowed = VehicleFactory.get_vehicles(user_weather.allowed_vehicles)
    orbits = [ORBIT1, ORBIT2]
    weather_adjusted_orbits = user_weather.adjust_orbits(orbits)
    decision = DecisionMaker().find_quickest_orbit_and_vehicle(vehicles_allowed, weather_adjusted_orbits)
    print(decision[0].vehicle_type)
    print(decision[1].name)







