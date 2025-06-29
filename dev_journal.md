---
**Journal Entry: MyFirstNFT (Core Token Standard)**

* **Project Name:** MyFirstNFT
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 29, 2025, 03:00:00 PM UTC
* **Contract Addresses:** 0x931911536239a641d04bc4C4cc5D589EC26304B6
* **Verification Status:** Verification Failed (The deployed and recompiled bytecode don't match, and error decoding response body from Sourcify API.)
* **Purpose:** This project demonstrates the deployment and basic interaction with an ERC-721 compliant Non-Fungible Token (NFT) contract. It showcases how to create a unique digital asset on the Monad Testnet, with ownership managed by the contract deployer.
* **Key Functions Demonstrated:**
    * `constructor()`: Initializes the ERC-721 contract with a name ("MyFirstNFT") and symbol ("MFN").
    * `safeMint(address to)`: Allows the contract owner to mint a new NFT and assign it to a specified recipient address. It uses OpenZeppelin's `Counters` library to manage unique token IDs.
* **Associated Components:**
    * **Frontend (HTML/JS):** A simple HTML page (`index.html`) that allows users to connect their MetaMask wallet, view the NFT contract's name and symbol, and mint new NFTs by providing a recipient address. It uses Ethers.js for Web3 interaction.
    * **Off-chain Script (Python):** A Python script (`mint_nft.py`) using `web3.py` to programmatically connect to the Monad Testnet, retrieve contract details (name, symbol), and mint an NFT to a specified address. This demonstrates off-chain interaction with the deployed smart contract.
* **How it was made:** The smart contract (`MyFirstNFT.sol`) was written in Solidity, inheriting from OpenZeppelin's `ERC721` and `Ownable` contracts for standard compliance and access control. It was compiled and deployed to the Monad Testnet using Hardhat. The deployment script (`scripts/deploy_nft.js`) was modified to correctly deploy the contract. Foundry's `forge verify-contract` was used to attempt verification on Sourcify, though it encountered issues. A basic HTML/JavaScript frontend (`index.html`) was created to provide a user interface for interaction, and a Python script (`mint_nft.py`) was developed for off-chain programmatic interaction.
* **Creative Decisions:** The project was kept simple to focus on the core concepts of ERC-721 NFT creation and basic interaction. The `safeMint` function was restricted to `onlyOwner` to illustrate a common access control pattern for initial NFT minting. The frontend and off-chain script were designed to be minimal but functional, demonstrating how to connect to the blockchain, read contract data, and send transactions. The use of OpenZeppelin contracts ensures adherence to best practices and security standards.

---
