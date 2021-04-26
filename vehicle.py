class Vehicle:
    def __init__(self, vehicle_type, speed, crater_time):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.crater_time = crater_time

    def influenced_by(self, orbit):
        return Vehicle("Bike", 10, 2)
