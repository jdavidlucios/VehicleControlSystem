from vehicle import Vehicle
from toll_booth import TollBooth
from solana_client import SolanaClient

# Create a new Solana client
solana_client = SolanaClient()

# Instantiate vehicle and toll booth
vehicle = Vehicle("Toyota", "Corolla", 2020, "ABC123", balance=100)
toll_booth = TollBooth("Downtown", toll_rate=5)

# Process toll payment
toll_booth.process_payment(vehicle, solana_client)
