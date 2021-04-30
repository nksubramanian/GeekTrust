from vehicle import VehicleType


class TravelOptionSelector:
    def select(self, travel_options):
        travel_options = self.__get_fastest_travel_options(travel_options)
        return self.__get_best_travel_option_based_on_vehicle(travel_options)

    def __get_fastest_travel_options(self, travel_options):
        travel_times = list(map(lambda x: x.get_travel_time(), travel_options))
        fastest_travel_time = min(travel_times)
        fastest_routes = list(filter(lambda x: x.get_travel_time() == fastest_travel_time, travel_options))
        return fastest_routes

    def __get_best_travel_option_based_on_vehicle(self, travel_options):
        for travel_option in travel_options:
            self.__rank_travel_options_on_vehicle(travel_option)

        minimum_rank = min(map(lambda x: x.rank, travel_options))
        best_ranked_travel_options = list(filter(lambda x: x.rank == minimum_rank, travel_options))
        return best_ranked_travel_options[0]

    def __rank_travel_options_on_vehicle(self, travel_option):
        ranking = {
            VehicleType.BIKE: 1,
            VehicleType.TUKTUK: 2,
            VehicleType.CAR: 3
        }
        rank = ranking[travel_option.get_vehicle()]
        travel_option.rank = rank