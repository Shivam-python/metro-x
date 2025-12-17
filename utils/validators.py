from config.constants import PASSENGER_TYPES, STATIONS

def validate_passenger(p):
    if p not in PASSENGER_TYPES:
        raise ValueError("INVALID PASSENGER TYPE")

def validate_station(s):
    if s not in STATIONS:
        raise ValueError("INVALID STATION")
