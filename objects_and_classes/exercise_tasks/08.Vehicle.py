class Vehicle:
    def __init__(self, vehicle_type, model, price):
        self.vehicle_type = vehicle_type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.vehicle_type}. Change: {money - self.price}"
        if self.owner is not None:
            return "Car already sold"
        elif money < self.price:
            return f"Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.vehicle_type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.vehicle_type} is on sale: {self.price}"

