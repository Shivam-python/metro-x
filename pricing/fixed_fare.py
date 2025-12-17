from pricing.fare_strategy import FareStrategy
from config.constants import *

BASE_FARES = {
    ADULT: 200,
    SENIOR: 100,
    KID: 50
}

class FixedFareStrategy(FareStrategy):
    def get_fare(self, passenger_type, journey_type):
        base = BASE_FARES[passenger_type]
        if journey_type == RETURN:
            return int(base * DISCOUNT_RATE)
        return base
