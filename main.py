from orbit import Orbit
from weather import Weather
from vehicle import Vehicle

if __name__ == '__main__':
    ORBIT1 = Orbit("ORBIT1", 18, 20, 89)
    ORBIT2 = Orbit("ORBIT2", 20, 10, 25)
    Bike = Vehicle("Bike", 10, 2)
    x = Bike.influenced_by(ORBIT1)

    Sunny = Weather("Sunny", -10, ["Car", "Bike", "TukTuk"])
    t = Sunny.effect(ORBIT1)
    print(t.no_of_craters)
    temp = Sunny.is_vehicle_allowed(Bike)
    print(temp)





