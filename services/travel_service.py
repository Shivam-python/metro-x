from domain.card import MetroCard
from domain.journey import Journey
from config.constants import *
from utils.validators import validate_passenger, validate_station

class TravelService:
    def __init__(self, fare_strategy, accounting):
        self.cards = {}
        self.fare_strategy = fare_strategy
        self.accounting = accounting

    def add_card(self, number, balance):
        self.cards[number] = MetroCard(number, balance)

    def check_in(self, card_no, passenger_type, origin):
        validate_passenger(passenger_type)
        validate_station(origin)

        card = self.cards[card_no]
        destination = AIRPORT if origin == CENTRAL else CENTRAL
        route = (origin, destination)

        journey_type = Journey.detect(
            card.last_route["route"] if card.last_route else None,
            route,
            journey_type=card.last_route["journey_type"] if card.last_route else None
        )

        fare = self.fare_strategy.get_fare(passenger_type, journey_type)

        if not card.deduct(fare):
            recharge = fare - card.balance
            service_charge = card.recharge(recharge, SERVICE_CHARGE_RATE)
            self.accounting.stats[origin]["income"] += service_charge
            card.deduct(fare)

        discount = 0
        if journey_type == RETURN:
            forward_fare = self.fare_strategy.get_fare(passenger_type, FORWARD)
            discount = forward_fare - fare

        self.accounting.record_trip(origin, fare, discount, passenger_type)

        card.last_route = {"route": route, "journey_type": journey_type}
