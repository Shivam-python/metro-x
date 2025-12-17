from config.constants import PASSENGER_TYPES

class AccountingService:
    def __init__(self, stations):
        self.stats = {
            s: {
                "income": 0,
                "discount": 0,
                **{p: 0 for p in PASSENGER_TYPES}
            } for s in stations
        }

    def record_trip(self, station, fare, discount, passenger_type):
        self.stats[station]["income"] += fare
        self.stats[station]["discount"] += discount
        self.stats[station][passenger_type] += 1
