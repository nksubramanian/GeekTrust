import sys
from assistance import Assistance


if __name__ == '__main__':
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    assistance = Assistance()
    travel_option = assistance.get_best_travel_option(inputs[0], [inputs[1], inputs[2]])
    print(travel_option.get_travel_details())










