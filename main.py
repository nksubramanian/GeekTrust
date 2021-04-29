import json
import sys
from travel_option_provider import TravelOptionProvider
from orbit import OrbitRepository


def get_best_travel_option(weather_string, orbit_speed_limits, parameters_of_orbits):
    orbit_repository = OrbitRepository(parameters_of_orbits)
    provider = TravelOptionProvider(orbit_repository)
    return provider.get_best_travel_option(weather_string, orbit_speed_limits)


def get_orbit_parameters(file_location):
    try:
        with open(file_location, 'r') as fp:
            json_object = json.load(fp)
            return json_object.get("orbits", "")
    except FileNotFoundError as error:
        return error.args[0]


def get_inputs():
    try:
        if len(sys.argv) != 2:
            raise AttributeError
        file_location = sys.argv[1]
        f = open(file_location, "r")
        inputs_from_file = f.readline().split()
        if inputs_from_file[0] not in ["SUNNY", "WINDY", "RAINY"]:
            raise AttributeError
        return inputs_from_file
    except FileNotFoundError as error:
        return error.args[0]
    except AttributeError:
        print("Attribute Error Raised")


if __name__ == '__main__':
    inputs = get_inputs()
    orbits_parameters = get_orbit_parameters("configurations.json")
    travel_option = get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])], orbits_parameters)
    print(travel_option.get_vehicle())
    print(travel_option.get_orbit())
