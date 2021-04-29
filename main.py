import json
import sys
from assistance import TravelOptionProvider


class UserInputError(Exception):
    pass


def get_best_travel_option(weather_string, orbit_speed_limits):
    # read config for orbit
    # create orbit repository with read config
    # pass the orbit repository to TravelOPtionProvider
    provider = TravelOptionProvider()
    return provider.get_best_travel_option(weather_string, orbit_speed_limits)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise UserInputError("please enter the file location as second location")
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    if inputs[0] not in ["SUNNY", "WINDY", "RAINY"]:
        raise UserInputError("Weather entered is incorrect")
    travel_option = get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])])
    print(travel_option.get_vehicle())
    print(travel_option.get_orbit())
    with open("./example.json", 'r') as fp:
        # F:\GeekTrust
        myObj = json.load(fp)
        x = myObj.get("orbit1", "")
        print(type(x[1]))
        print(x)


    # read config for orbit
    # create orbit repository with read config
    # pass the orbit repository to TravelOPtionProvider


