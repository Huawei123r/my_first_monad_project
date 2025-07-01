---
**Journal Entry: Multi-Sig Wallet (Governance)**

* **Project Name:** Multi-Sig Wallet
* **Category:** Governance
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 01, 2025, 11:52:00 AM UTC
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x3EA0598cc4fB26aECD93f31F26416DB7C0DCd10a
* **Key Files Created:**
    * `contracts/MultiSigWallet.sol`
    * `scripts/deploy_multi_sig_wallet.js`
* **Project Summary:** This project implements a multi-signature wallet that allows a group of owners to manage a shared wallet. It requires a certain number of owners to confirm a transaction before it can be executed.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Hardhat, Foundry
    * Key Libraries: None
    * Interaction Instructions: Use Hardhat tasks to interact with the contract.
* **Verification Status:** Verification Failed (Blockscout verifier returned an HTML page instead of a JSON response).
* **Verification Command (if applicable):** `/home/administrator/.foundry/bin/forge verify-contract --chain 10143 --verifier blockscout --verifier-url https://testnet.monadexplorer.com/api --compiler-version 0.8.20 0x3EA0598cc4fB26aECD93f31F26416DB7C0DCd10a contracts/MultiSigWallet.sol:MultiSigWallet --rpc-url https://testnet-rpc.monad.xyz/`
---
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
---
**Journal Entry: Counter Contract (Basic Utility)**

* **Project Name:** Counter Contract
* **Category:** Basic Utility
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 01, 2025 at 01:12:02 PM
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x299Cca24361b9a5437494c34622F5BB65312CdD1
* **Key Files Created:**
    * 
    * 
* **Project Summary:** A simple smart contract that allows users to increment and decrement a numerical counter. This demonstrates basic contract deployment and state management on the Monad Testnet.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.
        3. To read the current counter value:
           
        4. To increment the counter (requires gas):
           
        5. To decrement the counter (requires gas):
           
* **Verification Status:** Verified
* **Verification Command (if applicable):** 
---
---
**Journal Entry: Counter Contract (Basic Utility)**

* **Project Name:** Counter Contract
* **Category:** Basic Utility
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 01, 2025 at 01:12:11 PM
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x299Cca24361b9a5437494c34622F5BB65312CdD1
* **Key Files Created:**
    * 
    * 
* **Project Summary:** A simple smart contract that allows users to increment and decrement a numerical counter. This demonstrates basic contract deployment and state management on the Monad Testnet.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.
        3. To read the current counter value:
           
        4. To increment the counter (requires gas):
           
        5. To decrement the counter (requires gas):
           
* **Verification Status:** Verified
* **Verification Command (if applicable):** 
------\n**Journal Entry: Counter Contract (Basic Utility)**\n\n* **Project Name:** Counter Contract\n* **Category:** Basic Utility\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:13:19 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x299Cca24361b9a5437494c34622F5BB65312CdD1\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** A simple smart contract that allows users to increment and decrement a numerical counter. This demonstrates basic contract deployment and state management on the Monad Testnet.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: forge-std\n    * Interaction Instructions:\n        1. Ensure you have Foundry installed and configured.\n        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.\n        3. To read the current counter value:\n           \n        4. To increment the counter (requires gas):\n           \n        5. To decrement the counter (requires gas):\n           \n* **Verification Status:** Verified\n* **Verification Command (if applicable):** \n------\n**Journal Entry: MyFirstToken (Core Token Standard)**\n\n* **Project Name:** MyFirstToken\n* **Category:** Core Token Standard\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:14:08 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std\n    * Interaction Instructions:\n        1. Ensure you have Foundry installed and configured.\n        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.\n        3. To check the total supply:\n           \n        4. To check your balance:\n           \n        5. To mint new tokens (only by owner):\n           \n* **Verification Status:** Verified\n* **Verification Command (if applicable):** \n------\n**Journal Entry: MyFirstToken (Core Token Standard)**\n\n* **Project Name:** MyFirstToken\n* **Category:** Core Token Standard\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:14:35 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std\n    * Interaction Instructions:\n        1. Ensure you have Foundry installed and configured.\n        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.\n        3. To check the total supply:\n           \n        4. To check your balance:\n           \n        5. To mint new tokens (only by owner):\n           \n* **Verification Status:** Verified\n* **Verification Command (if applicable):** \n------\n**Journal Entry: MyFirstToken (Core Token Standard)**\n\n* **Project Name:** MyFirstToken\n* **Category:** Core Token Standard\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:14:49 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std\n    * Interaction Instructions:\n        1. Ensure you have Foundry installed and configured.\n        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.\n        3. To check the total supply:\n           \n        4. To check your balance:\n           \n        5. To mint new tokens (only by owner):\n           \n* **Verification Status:** Verified\n* **Verification Command (if applicable):** \n------
**Journal Entry: MyFirstToken (Core Token Standard)**

* **Project Name:** MyFirstToken
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 01, 2025 at 01:16:14 PM
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790
* **Key Files Created:**
    * `contracts/MyFirstToken.sol`
    * `scripts/DeployMyFirstToken.s.sol`
* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To check the total supply:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "totalSupply\(\)\(uint256\)"`
        4. To check your balance:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "balanceOf\(address\)\(uint256\)" YOUR_ADDRESS`
        5. To mint new tokens (only by owner):
           `cast send 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "mint\(address,uint256\)" RECIPIENT_ADDRESS AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployMyFirstToken.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key \$PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/MyFirstToken.sol -vvvv`
------
**Journal Entry: MyFirstToken (Core Token Standard)**

* **Project Name:** MyFirstToken
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 01, 2025 at 01:16:51 PM
* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790
* **Key Files Created:**
    * `contracts/MyFirstToken.sol`
    * `scripts/DeployMyFirstToken.s.sol`
* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To check the total supply:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "totalSupply()(uint256)"`
        4. To check your balance:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "balanceOf(address)(uint256)" YOUR_ADDRESS`
        5. To mint new tokens (only by owner):
           `cast send 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "mint(address,uint256)" RECIPIENT_ADDRESS AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployMyFirstToken.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key \$PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/MyFirstToken.sol -vvvv`
------\n**Journal Entry: MyFirstNFT (Core Token Standard)**\n\n* **Project Name:** MyFirstNFT\n* **Category:** Core Token Standard\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:17:51 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** N/A (Deployment Failed)\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** This project attempts to deploy a basic ERC-721 NFT contract named 'MyFirstNFT' with the symbol 'MNFT'. It includes a safe minting function accessible only by the contract owner.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: OpenZeppelin (ERC721, Ownable, Counters), forge-std\n    * Interaction Instructions: Deployment failed due to insufficient balance.\n* **Verification Status:** Not Applicable (Deployment Failed)\n* **Verification Command (if applicable):** N/A\n------\n**Journal Entry: SecondToken (Core Token Standard)**\n\n* **Project Name:** SecondToken\n* **Category:** Core Token Standard\n* **Network:** Monad Testnet\n* **Deployment Timestamp:** July 01, 2025 at 01:18:46 PM\n* **GitHub Repository URL:** https://github.com/orgs/community/discussions/22534\n* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x11C3F7863d7A2cee3BCE4e68B381493b1589EB3d\n* **Key Files Created:**\n    * \n    * \n* **Project Summary:** This project deploys a basic ERC-20 token named 'SecondToken' with the symbol 'SCT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.\n* **Technical Details:**\n    * Solidity Version: 0.8.20\n    * Framework Used: Foundry\n    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std\n    * Interaction Instructions:\n        1. Ensure you have Foundry installed and configured.\n        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a  file.\n        3. To check the total supply:\n           \n        4. To check your balance:\n           \n        5. To mint new tokens (only by owner):\n           \n* **Verification Status:** Verified\n* **Verification Command (if applicable):** \n---