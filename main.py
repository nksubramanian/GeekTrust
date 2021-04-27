from assistance import Assistance


if __name__ == '__main__':
    f = open("C:\\Users\\subra\\OneDrive\\Desktop\\file\\demofile.txt ", "r")
    f.readline()
    assistance = Assistance("Sunny", 89, 76)
    print(assistance.get_fastest_vehicle_and_route())










