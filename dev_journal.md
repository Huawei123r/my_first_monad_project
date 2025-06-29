---
**Journal Entry: MyFirstToken (Core Token Standard)**

* **Project Name:** MyFirstToken
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 29, 2025, 03:05:00 PM UTC
* **Contract Addresses:** 0x9Eb4d5A6eD8199751c730Bd653CC3C21760C152b
* **Verification Status:** Verification Failed (The deployed and recompiled bytecode don't match, and error decoding response body from Sourcify API.)
* **Purpose:** This project demonstrates the deployment and basic interaction with an ERC-20 compliant Fungible Token contract. It showcases how to create a transferable digital currency on the Monad Testnet, with initial supply minted to the deployer and a function for the owner to mint additional tokens.
* **Key Functions Demonstrated:**
    * `constructor(uint256 initialSupply)`: Initializes the ERC-20 contract with a name ("MyFirstToken") and symbol ("MFT"), and mints the `initialSupply` to the deployer.
    * `mint(address to, uint256 amount)`: Allows the contract owner to mint new tokens and assign them to a specified recipient address.
    * `transfer(address to, uint256 amount)`: Standard ERC-20 function allowing token holders to transfer tokens to another address.
    * `balanceOf(address account)`: Standard ERC-20 function to query the balance of a given address.
    * `totalSupply()`: Standard ERC-20 function to query the total supply of tokens.
* **Associated Components:**
    * **Frontend (HTML/JS):** A simple HTML page (`index_token.html`) that allows users to connect their MetaMask wallet, view the token contract's name, symbol, total supply, and their own balance. It also provides interfaces to mint new tokens (owner only) and transfer tokens to other addresses. It uses Ethers.js for Web3 interaction.
    * **Off-chain Script (Python):** A Python script (`interact_token.py`) using `web3.py` to programmatically connect to the Monad Testnet, retrieve contract details (name, symbol, total supply), check the owner's balance, mint new tokens, and transfer tokens. This demonstrates comprehensive off-chain interaction with the deployed ERC-20 smart contract.
* **How it was made:** The smart contract (`MyFirstToken.sol`) was written in Solidity, inheriting from OpenZeppelin's `ERC20` and `Ownable` contracts for standard compliance and access control. It was compiled and deployed to the Monad Testnet using Hardhat. The deployment script (`scripts/deploy_token.js`) handles the initial supply. Foundry's `forge verify-contract` was used to attempt verification on Sourcify, encountering similar issues as the previous project. A basic HTML/JavaScript frontend (`index_token.html`) was created for user interaction, and a Python script (`interact_token.py`) was developed for off-chain programmatic interaction.
* **Creative Decisions:** This project expands on the basic token concept by adding a `mint` function for the owner, demonstrating a common pattern for managing token supply. The frontend provides both minting and transferring functionalities, offering a more complete user experience for an ERC-20 token. The Python script covers reading various token properties and executing both minting and transfer transactions, showcasing a broader range of off-chain interactions.

---