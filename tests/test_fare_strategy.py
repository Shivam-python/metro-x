from pricing.fixed_fare import FixedFareStrategy
from config.constants import ADULT, KID, FORWARD, RETURN

def test_forward_fare():
    strategy = FixedFareStrategy()
    assert strategy.get_fare(ADULT, FORWARD) == 200
    assert strategy.get_fare(KID, FORWARD) == 50

def test_return_fare_discount():
    strategy = FixedFareStrategy()
    assert strategy.get_fare(ADULT, RETURN) == 100
    assert strategy.get_fare(KID, RETURN) == 25
