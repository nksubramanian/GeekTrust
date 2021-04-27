import sys
from assistance import Assistance


if __name__ == '__main__':
    file_location = sys.argv[1]
    f = open(file_location, "r")
    inputs = f.readline().split()
    assistance = Assistance()
    print(assistance.get_fastest_vehicle_and_route(inputs[0], inputs[1], inputs[2]))










