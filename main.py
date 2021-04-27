import sys
from assistance import TravelOptionProvider


if __name__ == '__main__':
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    provider = TravelOptionProvider()
    travel_option = provider.get_best_travel_option(inputs[0], [int(inputs[1]), int(inputs[2])])
    print(travel_option.get_travel_details())










