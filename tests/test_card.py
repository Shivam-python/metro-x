from domain.card import MetroCard

def test_deduct_success():
    card = MetroCard("MC1", 500)
    assert card.deduct(200) is True
    assert card.balance == 300

def test_deduct_failure():
    card = MetroCard("MC2", 100)
    assert card.deduct(200) is False
    assert card.balance == 100

def test_recharge():
    card = MetroCard("MC3", 0)
    service_charge = card.recharge(100, 0.02)
    assert card.balance == 100
    assert service_charge == 2
