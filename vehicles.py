import uuid

class Vehicle:
    def __init__(self, brand: str, model: str, year: int, license_plate: str, balance: float = 0, iot_device_id: str = None):
        self.id = uuid.uuid4()  # Generate a unique ID for each object
        self.brand = brand
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.balance = balance
        self.iot_device_id = iot_device_id

    def pay_toll(self, toll_rate: float) -> bool:
        if self.balance >= toll_rate:
            self.balance -= toll_rate
            # Send payment confirmation to IoT device and toll management system
            return True
        return False

class Automobile(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toll_rate = 2.0  # default toll rate for automobiles

class Motorcycle(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toll_rate = 1.0  # default toll rate for motorcycles

class TollBooth:
    def __init__(self, toll_rate: float):
        self.toll_rate = toll_rate

    def collect_toll(self, vehicle: Vehicle) -> bool:
        if vehicle.pay_toll(self.toll_rate):
            print(f"Collected toll of {self.toll_rate} from {vehicle.license_plate}")
            return True
        print(f"Insufficient toll balance for {vehicle.license_plate}")
        return False