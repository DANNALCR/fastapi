from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def get_best_route(self, origin: int, destination: int) -> dict:
        pass

    @abstractmethod
    def get_cost(self, origin: int, destination: int) -> float:
        pass

    @abstractmethod
    def get_time(self, origin: int, destination: int) -> float:
        pass


class CarRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the avenue 123"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.1, 2)

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.5, 2)


class BikeRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the bike lane"}

    def get_cost(self, origin: int, destination: int) -> float:
        return 0

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 2, 2)


class MotorcycleRoute(RouteStrategy):
    def get_best_route(self, origin: int, destination: int) -> dict:
        return {"start_street": origin, "end_street": destination, "route": "Use the motorcycle lane"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.05, 2)

    def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.25, 2)


class HotelReservationStrategy(ABC):
    @abstractmethod
    def calculate_total_cost(self, num_nights: int, euro_rate: float) -> float:
        pass


class BasicHotelReservation(HotelReservationStrategy):
    def calculate_total_cost(self, num_nights: int, euro_rate: float) -> float:
        return round(num_nights * 100 * euro_rate, 2)


class LuxuryHotelReservation(HotelReservationStrategy):
    def calculate_total_cost(self, num_nights: int, euro_rate: float) -> float:
        return round(num_nights * 200 * euro_rate, 2)


if __name__ == "__main__":
    # Example of using CarRoute
    car_route = CarRoute()
    origin = 10
    destination = 30
    print("Car Route:", car_route.get_best_route(origin, destination))
    print("Cost:", car_route.get_cost(origin, destination))
    print("Time:", car_route.get_time(origin, destination))

    # Example of using BasicHotelReservation
    basic_reservation = BasicHotelReservation()
    num_nights = 3
    euro_rate = 4200  # Exchange rate: 1 euro = 4200 pesos colombianos
    total_cost_colombian_pesos = basic_reservation.calculate_total_cost(num_nights, euro_rate)
    print("Basic Hotel Reservation Total Cost (in Colombian Pesos):", total_cost_colombian_pesos)

