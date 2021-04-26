class DecisionMaker:
    @staticmethod
    def find_quickest_orbit_and_vehicle(vehicle_types, orbits):
        time = []
        for vehicle_type in vehicle_types:
            time.append(vehicle_type.compute_time_for_orbits(orbits))
        min_position_for_each_row = []
        horizontal_indices = []
        for iterator in time:
            min_position_for_each_row.append(min(iterator))
            horizontal_indices.append(iterator.index(min(iterator)))
        required_min = min(min_position_for_each_row)
        horizontal_index = min_position_for_each_row.index(required_min)
        vertical_index = horizontal_indices[horizontal_index]
        return [vehicle_types[horizontal_index], orbits[vertical_index]]




