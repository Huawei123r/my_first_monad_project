# My First Monad Project Portfolio

Welcome to the Monad Project Portfolio! This repository showcases a collection of decentralized applications and smart contracts deployed on the Monad Testnet. Each project demonstrates different aspects of Web3 development, from core token standards to DeFi primitives and security patterns.

## Projects Overview

Here's a summary of the projects included in this portfolio:

### Counter Contract (Basic Utility)
*   **Project Summary:** A simple smart contract that allows users to increment and decrement a numerical counter. This demonstrates basic contract deployment and state management on the Monad Testnet.
*   **Deployed Address:** [0x299Cca24361b9a5437494c34622F5BB65312CdD1](https://testnet.monadexplorer.com/address/0x299Cca24361b9a5437494c34622F5BB65312CdD1)
*   **Key Files:** [`contracts/Counter.sol`](./contracts/Counter.sol), [`scripts/DeployCounter.s.sol`](./scripts/DeployCounter.s.sol)
*   **Status:** Verified

### MyFirstToken (Core Token Standard)
*   **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.
*   **Deployed Address:** [0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790](https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790)
*   **Key Files:** [`contracts/MyFirstToken.sol`](./contracts/MyFirstToken.sol), [`scripts/DeployMyFirstToken.s.sol`](./scripts/DeployMyFirstToken.s.sol)
*   **Status:** Verified

### SecondToken (Core Token Standard)
*   **Project Summary:** This project deploys a basic ERC-20 token named 'SecondToken' with the symbol 'SCT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.
*   **Deployed Address:** [0x11C3F7863d7A2cee3BCE4e68B381493b1589EB3d](https://testnet.monadexplorer.com/address/0x11C3F7863d7A2cee3BCE4e68B381493b1589EB3d)
*   **Key Files:** [`contracts/SecondToken.sol`](./contracts/SecondToken.sol), [`scripts/DeploySecondToken.s.sol`](./scripts/DeploySecondToken.s.sol)
*   **Status:** Verified

### SimpleDEX (Basic DeFi Protocol)
*   **Project Summary:** This project deploys a basic Decentralized Exchange (DEX) contract that allows for swapping between two ERC-20 tokens (MyFirstToken and SecondToken). It includes functions for adding liquidity and performing swaps based on a simple x*y=k constant product formula.
*   **Deployed Address:** [0xe0cba59A3186Fe5f3c9053e82d2855BFD537c850](https://testnet.monadexplorer.com/address/0xe0cba59A3186Fe5f3c9053e82d2855BFD537c850)
*   **Key Files:** [`contracts/SimpleDEX.sol`](./contracts/SimpleDEX.sol), [`scripts/DeploySimpleDEX.s.sol`](./scripts/DeploySimpleDEX.s.sol)
*   **Status:** Verified

### Pausable Contract (Security Pattern)
*   **Project Summary:** This project implements a pausable contract, allowing the owner to pause and unpause certain contract functionalities. This is a common security pattern to mitigate risks during upgrades or in case of emergencies.
*   **Deployed Address:** [0x5924f8fD5aA85Dd40b53F43AE8ea482cD84B906A](https://testnet.monadexplorer.com/address/0x5924f8fD5aA85Dd40b53F43AE8ea482cD84B906A)
*   **Key Files:** [`contracts/PausableContract.sol`](./contracts/PausableContract.sol), [`scripts/DeployPausableContract.s.sol`](./scripts/DeployPausableContract.s.sol)
*   **Status:** Verified

### MyFirstNFT (Core Token Standard)
*   **Project Summary:** This project deploys a basic ERC-721 NFT contract named 'MyFirstNFT' with the symbol 'MNFT'. It includes a safe minting function accessible only by the contract owner.
*   **Deployed Address:** [0xf8b5d80c2dBebCD3c59Ce62FB5515D97e7412E8a](https://testnet.monadexplorer.com/address/0xf8b5d80c2dBebCD3c59Ce62FB5515D97e7412E8a)
*   **Key Files:** [`contracts/MyFirstNFT.sol`](./contracts/MyFirstNFT.sol), [`scripts/DeployMyFirstNFT.s.sol`](./scripts/DeployMyFirstNFT.s.sol)
*   **Status:** Verified

### Time-Locked Wallet (Basic Utility)
*   **Project Summary:** This project implements a time-locked wallet that allows users to deposit ETH or ERC-20 tokens, which can only be withdrawn after a specified unlock time. The owner can set the unlock time for any user.
*   **Deployed Address:** [0xa226E8D4F997ce60e22300455405a0a54c93D91D](https://testnet.monadexplorer.com/address/0xa226E8D4F997ce60e22300455405a0a54c93D91D)
*   **Key Files:** [`contracts/TimeLockedWallet.sol`](./contracts/TimeLockedWallet.sol), [`scripts/DeployTimeLockedWallet.s.sol`](./scripts/DeployTimeLockedWallet.s.sol)
*   **Status:** Verified

### Reentrancy Guard (Security Pattern)
*   **Project Summary:** This project implements a contract with a reentrancy guard, a security pattern to prevent reentrancy attacks. It includes basic deposit and withdraw functions protected by the `nonReentrant` modifier.
*   **Deployed Address:** [0xa502Fe7A4f5B0f9e369Ad3260d6808Cec9a507DC](https://testnet.monadexplorer.com/address/0xa502Fe7A4f5B0f9e369Ad3260d6808Cec9a507DC)
*   **Key Files:** [`contracts/ReentrancyGuard.sol`](./contracts/ReentrancyGuard.sol), [`scripts/DeployReentrancyGuard.s.sol`](./scripts/DeployReentrancyGuard.s.sol)
*   **Status:** Verified

### TodoList (Simple Decentralized Application)
*   **Project Summary:** This project implements a simple decentralized to-do list application on the blockchain. Users can add, mark as complete, and delete tasks.
*   **Deployed Address:** [0xdf07ea1f7f4b042584475235A829afc2b43485E7](https://testnet.monadexplorer.com/address/0xdf07ea1f7f4b042584475235A829afc2b43485E7)
*   **Key Files:** [`contracts/TodoList.sol`](./contracts/TodoList.sol), [`scripts/DeployTodoList.s.sol`](./scripts/DeployTodoList.s.sol)
*   **Status:** Verified

### Box (Upgradeable Contract)
*   **Project Summary:** An upgradeable contract using the UUPS proxy pattern. It stores a single `uint256` value that can be updated by the owner. This contract has been upgraded to `BoxV2` to include an `increment()` function.
*   **Deployed Address:** [0x61DE40ee9DA523A96Da02A5521c4122B69EFF22C](https://testnet.monadexplorer.com/address/0x61DE40ee9DA523A96Da02A5521c4122B69EFF22C)
*   **Key Files:** [`contracts/Box.sol`](./contracts/Box.sol), [`contracts/BoxV2.sol`](./contracts/BoxV2.sol), [`scripts/DeployBox.s.sol`](./scripts/DeployBox.s.sol), [`scripts/DeployBoxV2.s.sol`](./scripts/DeployBoxV2.s.sol)
*   **Status:** Verified

### Crowdsale 2 (Basic DeFi Protocol)
*   **Project Summary:** This project deploys a basic Decentralized Exchange (DEX) contract that allows for swapping between two ERC-20 tokens (MyFirstToken and SecondToken). It includes functions for adding liquidity and performing swaps based on a simple x*y=k constant product formula.
*   **Deployed Address:** [0x865ffa8b472856210b66586017437dc4DbD3A749](https://testnet.monadexplorer.com/address/0x865ffa8b472856210b66586017437dc4DbD3A749)
*   **Key Files:** [`contracts/Crowdsale.sol`](./contracts/Crowdsale.sol), [`scripts/DeployCrowdsale2.s.sol`](./scripts/DeployCrowdsale2.s.sol)
*   **Status:** Verified

### Escrow (Basic Utility)
*   **Project Summary:** This project deploys an Escrow contract that holds funds for a beneficiary, releasable after a deadline.
*   **Deployed Address:** [0x5CCA4e566b5830c0AB017B21389E877CC8DF7150](https://testnet.monadexplorer.com/address/0x5CCA4e566b5830c0AB017B21389E877CC8DF7150)
*   **Key Files:** [`contracts/Escrow.sol`](./contracts/Escrow.sol), [`scripts/DeployEscrow.s.sol`](./scripts/DeployEscrow.s.sol)
*   **Status:** Verified

### EventLogger 2 (Off-Chain Data / Indexing Focus)
*   **Project Summary:** This project deploys a simple contract for logging events on the blockchain.
*   **Deployed Address:** [0xAc3275D6cE832e3b3ac32622C4040c10a87CFc67](https://testnet.monadexplorer.com/address/0xAc3275D6cE832e3b3ac32622C4040c10a87CFc67)
*   **Key Files:** [`contracts/EventLogger.sol`](./contracts/EventLogger.sol), [`scripts/DeployEventLogger2.s.sol`](./scripts/DeployEventLogger2.s.sol)
*   **Status:** Verified

### Faucet (Basic Utility)
*   **Project Summary:** This project deploys a Faucet contract that distributes a fixed amount of ERC20 tokens to users once per day.
*   **Deployed Address:** [0x88fCdCA4af91b3BAC58c27AE2FD835B8c89392Ef](https://testnet.monadexplorer.com/address/0x88fCdCA4af91b3BAC58c27AE2FD835B8c89392Ef)
*   **Key Files:** [`contracts/Faucet.sol`](./contracts/Faucet.sol), [`scripts/DeployFaucet.s.sol`](./scripts/DeployFaucet.s.sol)
*   **Status:** Verified

## Getting Started

To explore these projects locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Huawei123r/my_first_monad_project.git
    cd my_first_monad_project
    ```

2.  **Install Foundry:**
    If you don't have Foundry installed, follow the instructions [here](https://book.getfoundry.sh/getting-started/installation).

3.  **Install Node.js dependencies (for Hardhat projects, if any):**
    ```bash
    npm install
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your `PRIVATE_KEY` and `MONAD_RPC_URL` (e.g., `https://testnet-rpc.monad.xyz`). You can obtain testnet funds from the [Monad Testnet Faucet](https://testnet.monad.xyz).

5.  **Build Contracts:**
    ```bash
    forge build
    ```

6.  **Interact with Deployed Contracts:**
    Refer to the `dev_journal.md` file for specific interaction instructions for each deployed contract using `cast` commands.

## Development Journal

For detailed deployment information, including timestamps, transaction hashes, and verification commands, please refer to the [`dev_journal.md`](./dev_journal.md) file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
