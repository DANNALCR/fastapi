from fastapi import APIRouter, Depends, HTTPException
from .strategy import CarRoute, BikeRoute, RouteStrategy, MotorcycleRoute
from .hotel_strategy import BasicHotelReservation, HotelReservationStrategy, LuxuryHotelReservation
from enum import Enum

class Vehicle(Enum):
    CAR = "car"
    BIKE = "bike"
    MOTORCYCLE = "motorcycle"

class Currency(Enum):
    EURO = "euro"
    # Add more currencies as needed

def get_strategy(vehicle: Vehicle) -> RouteStrategy:
    if vehicle == Vehicle.CAR:
        return CarRoute()
    elif vehicle == Vehicle.BIKE:
        return BikeRoute()
    elif vehicle == Vehicle.MOTORCYCLE:
        return MotorcycleRoute()
    else:
        raise HTTPException(status_code=400, detail="Invalid vehicle")

def get_currency(currency: Currency) -> float:
    if currency == Currency.EURO:
        # Here you can fetch the current exchange rate from a service or database
        # For simplicity, I'm hardcoding it here
        return 4200  # 1 euro = 4200 pesos colombianos
    else:
        raise HTTPException(status_code=400, detail="Invalid currency")

router = APIRouter()

@router.get("/best_route")
def best_route(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, currency: Currency = Currency.EURO,
               route_strategy: RouteStrategy = Depends(get_strategy)) -> dict:
    return route_strategy.get_best_route(origin=origin, destination=destination)

@router.get("/cost")
def cost(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, currency: Currency = Currency.EURO,
         route_strategy: RouteStrategy = Depends(get_strategy)) -> float:
    if vehicle == Vehicle.CAR:
        return route_strategy.get_cost(origin=origin, destination=destination)
    elif vehicle in [Vehicle.BIKE, Vehicle.MOTORCYCLE]:
        return 0  # No cost for bike or motorcycle routes
    else:
        raise HTTPException(status_code=400, detail="Invalid vehicle")

@router.get("/time")
def time(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, currency: Currency = Currency.EURO,
         route_strategy: RouteStrategy = Depends(get_strategy)) -> float:
    return route_strategy.get_time(origin=origin, destination=destination)

@router.get("/hotel_cost")
def hotel_cost(num_nights: int, hotel_type: str, currency: Currency = Currency.EURO,
               hotel_strategy: HotelReservationStrategy = Depends(BasicHotelReservation)) -> float:
    if hotel_type == "basic":
        return hotel_strategy.calculate_total_cost(num_nights=num_nights, euro_rate=get_currency(currency))
    elif hotel_type == "luxury":
        return hotel_strategy.calculate_total_cost(num_nights=num_nights, euro_rate=get_currency(currency)) * 2
    else:
        raise HTTPException(status_code=400, detail="Invalid hotel type")