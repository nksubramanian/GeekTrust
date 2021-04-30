import json
import sys
from travel_option_provider import TravelOptionProvider
from orbit import OrbitRepository


def get_best_travel_option(weather_string, orbit_speed_limits, parameters_of_orbits):
    orbit_repository = OrbitRepository(parameters_of_orbits)
    provider = TravelOptionProvider(orbit_repository)
    return provider.get_travel_option(weather_string, orbit_speed_limits)


def get_orbit_parameters(file_location):
    with open(file_location, 'r') as fp:
        json_object = json.load(fp)
        parameters_of_orbits = json_object.get("orbits")
        for orbit in parameters_of_orbits:
            if len(orbit) != 3:
                raise Exception("The number of orbit parameters has to be 3")
            elif type(orbit[0]) is not str:
                raise Exception("Orbit's distance and no of craters has to be integer")
            elif (type(orbit[1]) is not int) or (type(orbit[2]) is not int):
                raise Exception("Orbit's distance and no of craters has to be integer")
        return parameters_of_orbits


def get_inputs(file_location):
    f = open(file_location, "r")
    inputs_from_file = f.readline().split()
    return inputs_from_file

def main():
    if len(sys.argv) != 2:
        raise Exception(f"Expect main.py and <input file location> as arguments")
    inputs = get_inputs(sys.argv[1])
    if inputs[0] not in ["SUNNY", "WINDY", "RAINY"]:
        raise Exception("Unrecognized weather")
    orbits_parameters = get_orbit_parameters("./config/configurations.json")
    travel_option = get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])], orbits_parameters)
    print(f'{travel_option.get_vehicle().name} {travel_option.get_orbit()}')


if __name__ == '__main__':
    main()
