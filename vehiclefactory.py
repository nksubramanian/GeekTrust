from vehicle import Vehicle


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type_allowed):
        vehicle_list = []
        for vehicle in vehicle_type_allowed:
            if vehicle == "Bike":
                vehicle_list.append(Vehicle("Bike", 10, 0))
            if vehicle == "TukTuk":
                vehicle_list.append(Vehicle("TukTuk", 45, 0))
            if vehicle == "Car":
                vehicle_list.append(Vehicle("Car", 20, 0))
        return vehicle_list
