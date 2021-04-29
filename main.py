import json
import sys
from assistance import TravelOptionProvider
from orbit import OrbitRepository


class UserInputError(Exception):
    pass


def get_best_travel_option(weather_string, orbit_speed_limits, orbitparameters):
    orbit_repository = OrbitRepository(orbitparameters)
    provider = TravelOptionProvider(orbit_repository)
    return provider.get_best_travel_option(weather_string, orbit_speed_limits)


def get_orbit_parameters(file_location):
    with open(file_location, 'r') as fp:
        json_object = json.load(fp)
        x = json_object.get("orbit1", "")
        y = json_object.get("orbit2", "")
        return [x, y]

def get_inputs():
    if len(sys.argv) != 2:
        raise UserInputError("please enter the file location as second location")
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    if inputs[0] not in ["SUNNY", "WINDY", "RAINY"]:
        raise UserInputError("Weather entered is incorrect")
    return inputs



if __name__ == '__main__':
    inputs = get_inputs()
    orbit_parameters = get_orbit_parameters("./example.json")
    travel_option = get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])], orbit_parameters)
    print(travel_option.get_vehicle())
    print(travel_option.get_orbit())





