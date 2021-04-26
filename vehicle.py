class Vehicle:
    def __init__(self, vehicle_type, speed, crater_time):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.crater_time = crater_time

    @staticmethod
    def influenced_by(orbit):
        return Vehicle("Bike", 10, 2)
