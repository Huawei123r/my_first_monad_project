---
**Journal Entry: Escrow (DeFi)**

* **Project Name:** Escrow
* **Category:** DeFi
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 30, 2025, 07:28:00 AM UTC
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x471ac1C07De08c581441Df8170671e2E7a559171
* **Key Files Created:**
    * `contracts/Escrow.sol`
    * `scripts/deploy_escrow.js`
* **Project Summary:** This project implements a simple escrow contract that allows a depositor to send ether to a beneficiary. The funds are held in the contract until the beneficiary releases them. The depositor can also reclaim the funds after a deadline has passed.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Hardhat, Foundry
    * Key Libraries: None
    * Interaction Instructions: Use Hardhat tasks to interact with the contract.
* **Verification Status:** Verification Failed (Blockscout verifier returned an HTML page instead of a JSON response).
* **Verification Command (if applicable):** `/home/administrator/.foundry/bin/forge verify-contract --chain 10143 --verifier blockscout --verifier-url https://testnet.monadexplorer.com/api --compiler-version 0.8.20 0x471ac1C07De08c581441Df8170671e2E7a559171 contracts/Escrow.sol:Escrow --rpc-url https://testnet-rpc.monad.xyz/`
---
---
**Journal Entry: Faucet (DeFi)**

* **Project Name:** Faucet
* **Category:** DeFi
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 29, 2025, 03:25:00 PM UTC
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** 
    * Faucet: https://testnet.monadexplorer.com/address/0x51641A255351d2766425731c75a4CF6658fb1e2D
    * SimpleToken: https://testnet.monadexplorer.com/address/0xD38D9C6ceB4cb4664a5d3bAF88F75e3c778e8941
* **Key Files Created:**
    * `contracts/Faucet.sol`
    * `contracts/SimpleToken.sol`
    * `scripts/deploy_faucet.js`
* **Project Summary:** This project implements a simple ERC20 token faucet. It allows users to request a fixed amount of tokens once a day. The owner can set the withdrawal amount, withdraw the remaining tokens, withdraw any ether sent to the contract, and transfer ownership.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Hardhat, Foundry
    * Key Libraries: OpenZeppelin
    * Interaction Instructions: Use Hardhat tasks to interact with the contract. For example, to request tokens, you can use `npx hardhat request-tokens --faucet <faucet-address> --network monad`.
* **Verification Status:** Verification Failed (Blockscout verifier returned an HTML page instead of a JSON response).
* **Verification Command (if applicable):** 
    * SimpleToken: `/home/administrator/.foundry/bin/forge verify-contract --chain 10143 --verifier blockscout --verifier-url https://testnet.monadexplorer.com/api --compiler-version 0.8.20 0xD38D9C6ceB4cb4664a5d3bAF88F75e3c778e8941 contracts/SimpleToken.sol:SimpleToken --rpc-url https://testnet-rpc.monad.xyz/`
    * Faucet: `/home/administrator/.foundry/bin/forge verify-contract --chain 10143 --verifier blockscout --verifier-url https://testnet.monadexplorer.com/api --compiler-version 0.8.20 0x51641A255351d2766425731c75a4CF6658fb1e2D contracts/Faucet.sol:Faucet --rpc-url https://testnet-rpc.monad.xyz/`
---
---
**Journal Entry: Counter (Basic Utility)**

* **Project Name:** Counter
* **Category:** Basic Utility
* **Network:** Monad Testnet
* **Deployment Timestamp:** June 29, 2025, 03:10:00 PM UTC
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x535A7B41b15Aea6fa21c89Dd80C0035Acf5a9c06
* **Key Files Created:**
    * `contracts/Counter.sol`
    * `scripts/deploy_counter.js`
    * `index_counter.html`
* **Project Summary:** This project implements a simple counter smart contract, demonstrating basic state management and function calls on the blockchain. It allows users to increment, decrement and set a numerical value stored on-chain.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Hardhat, Foundry
    * Key Libraries: OpenZeppelin (not used in this contract)
    * Interaction Instructions: Open `index_counter.html` in a web browser with MetaMask installed. Connect your wallet to the Monad Testnet and interact with the contract using the buttons provided.
* **Verification Status:** Verification Failed (Sourcify and Blockscout verifiers returned errors).
* **Verification Command (if applicable):** `/home/administrator/.foundry/bin/forge verify-contract --chain 10143 --verifier blockscout --verifier-url https://testnet.monadexplorer.com/api --compiler-version 0.8.20 0x535A7B41b15Aea6fa21c89Dd80C0035Acf5a9c06 contracts/Counter.sol:Counter --rpc-url https://testnet-rpc.monad.xyz/`
---
