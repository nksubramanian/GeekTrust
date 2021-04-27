import sys
from assistance import TravelOptionProvider


def get_best_travel_option(weather_string, orbit_speed_limits):
    provider = TravelOptionProvider()
    return provider.get_best_travel_option(weather_string, orbit_speed_limits)


if __name__ == '__main__':
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    travel_option = get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])])
    print(travel_option.get_travel_details())










