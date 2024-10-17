class TollBooth:
    def __init__(self, location: str, toll_rate: float):
        self.location = location
        self.toll_rate = toll_rate

    def process_payment(self, vehicle, solana_client):
        if solana_client.trigger_toll_payment(vehicle.id, self.toll_rate):
            print(f"Payment successful for {vehicle.license_plate}")
        else:
            print("Payment failed: Insufficient balance.")
