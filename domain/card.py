class MetroCard:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
        self.last_route = None # {"route": (origin, destination), "journey_type": FORWARD/RETURN}
        self.history = []

    def deduct(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def recharge(self, amount, service_charge_rate):
        charge = int(amount * service_charge_rate)
        self.balance += amount
        return charge
