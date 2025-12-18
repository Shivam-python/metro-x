from domain.journey import Journey
from config.constants import FORWARD, RETURN

def test_first_journey_is_forward():
    route = ("CENTRAL", "AIRPORT")
    assert Journey.detect(None, route) == FORWARD

def test_return_journey():
    last_route = ("CENTRAL", "AIRPORT")
    last_journey_type = FORWARD
    current = ("AIRPORT", "CENTRAL")

    assert Journey.detect(last_route, current, last_journey_type) == RETURN