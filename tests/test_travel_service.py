from services.travel_service import TravelService
from services.accounting_service import AccountingService
from pricing.fixed_fare import FixedFareStrategy
from config.constants import *

def setup_service():
    accounting = AccountingService(STATIONS)
    service = TravelService(FixedFareStrategy(), accounting)
    return service, accounting

def test_forward_journey():
    service, accounting = setup_service()
    service.add_card("MC1", 500)

    service.check_in("MC1", ADULT, CENTRAL)

    stats = accounting.stats[CENTRAL]
    assert stats["income"] == 200
    assert stats["discount"] == 0
    assert stats[ADULT] == 1

def test_return_journey_discount():
    service, accounting = setup_service()
    service.add_card("MC1", 500)

    service.check_in("MC1", ADULT, CENTRAL)
    service.check_in("MC1", ADULT, AIRPORT)

    airport = accounting.stats[AIRPORT]
    assert airport["income"] == 100
    assert airport["discount"] == 100
    assert airport[ADULT] == 1

def test_insufficient_balance_triggers_recharge():
    service, accounting = setup_service()
    service.add_card("MC1", 0)

    service.check_in("MC1", ADULT, CENTRAL)

    stats = accounting.stats[CENTRAL]
    assert stats["income"] == 204  # 200 fare + 4 service charge
