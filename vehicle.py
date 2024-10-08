import uuid

class Vehicle:
    def __init__(self, brand: str, model: str, year: int, license_plate: str, balance: float = 0):
        self.id = uuid.uuid4()  # Generate unique UUID for the vehicle
        self.brand = brand
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.balance = balance
