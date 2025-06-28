
---
**Journal Entry: Simple ERC-20 Token (Core Token Standard)**

* **Project Name:** Simple ERC-20 Token
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 28, 2025, 10:30:00 AM UTC (Simulated)
* **Contract Addresses:** 0x5FbDB2315678afecb367f032d93F642f64180aa3 (Simulated Deployment Address)
* **Purpose:** To create a basic, fungible token compliant with the ERC-20 standard. This is a fundamental building block for many decentralized applications, representing everything from utility tokens to governance tokens.
* **Key Functions Demonstrated:**
    * `constructor`: Mints the initial supply to the deployer.
    * `transfer`: Allows token holders to send tokens to other addresses.
    * `approve` / `transferFrom`: Enables delegated token transfers.
* **Associated Components:**
    * **Frontend (HTML/JS):** N/A for this project.
    * **Off-chain Script (Python):** N/A for this project.
* **How it was made:** The contract was written in Solidity using the OpenZeppelin ERC20 implementation. It was compiled and deployed using Hardhat and a JavaScript deployment script.
* **Creative Decisions:** I chose to mint the entire initial supply to the deployer's address for simplicity. This is a common pattern for tokens where the founding team or organization controls the initial distribution.

---

---
**Journal Entry: Simple Counter (Basic Interaction)**

* **Project Name:** Simple Counter
* **Category:** Basic Interaction
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 28, 2025, 10:35:00 AM UTC (Simulated)
* **Contract Addresses:** 0x5FbDB2315678afecb367f032d93F642f64180aa3 (Simulated Deployment Address)
* **Purpose:** To demonstrate the most basic state change on a blockchain. The counter contract is a "hello world" of smart contracts, showing how to read and write data to the blockchain.
* **Key Functions Demonstrated:**
    * `increment`: Increases the public `count` variable by one.
    * `decrement`: Decreases the public `count` variable by one.
* **Associated Components:**
    * **Frontend (HTML/JS):** N/A for this project.
    * **Off-chain Script (Python):** N/A for this project.
* **How it was made:** The contract was written in Solidity. It was compiled and deployed using Hardhat and a JavaScript deployment script.
* **Creative Decisions:** The contract is intentionally minimal to focus on the core concept of state changes. There are no access controls or other features, making it easy to understand for beginners.

---
