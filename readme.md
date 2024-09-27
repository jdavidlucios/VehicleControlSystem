**System Overview**

This hybrid toll payment system leverages IoT technology and the Solana blockchain to autonomously process vehicle payments. Vehicles are identified by UUIDs, and their balances are managed on-chain using a Solana smart contract. The IoT-enabled vehicles communicate with toll booths, triggering a payment request that is sent to the blockchain. Python is used for off-chain logic, handling IoT device communication and interacting with the Solana blockchain to verify balances and process payments. Rust is used for the on-chain smart contract that manages the core toll payment logic, ensuring trustless and transparent transactions/balances.

**Technologies Used**

* Python: Handles off-chain logic and interacts with the Solana blockchain.
* Solana Blockchain (Rust): Manages vehicle balances and processes toll payments securely.
* UUID: Unique identification for vehicles in the system.
* IoT: Communicates vehicle data and triggers toll payments.

**How to Run the Project**

Set Up Solana Development Environment:

* Install Solana CLI and SDK.
* Write and deploy the smart contract to the Solana devnet.

Set Up Python Environment:

* Install Python dependencies:
  pip install -r requirements.txt

Run the Program:

* Execute main.py to simulate vehicle toll payment:
  python main.py

This structure should allow you to test the interaction between the Python off-chain logic and the Solana smart contract.

**License**

This is an open source proyect draft that you can copy, improve, test and/or implement freely. It's intended to be used within new decentralized 4.0 cities as part of their public infrastructure.