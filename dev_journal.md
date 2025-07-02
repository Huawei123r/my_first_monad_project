---
**Journal Entry: MyERC1155Token (Core Token Standard)**

* **Project Name:** MyERC1155Token
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 02, 2025 at 11:30:00 AM
* **GitHub Repository URL:** https://github.com/Huawei123r/my_first_monad_project
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0xcaa53094C46e34Acb10D642377047c149ae87CE1
* **Key Files Created:**
    * `contracts/MyERC1155Token.sol`
    * `scripts/DeployMyERC1155Token.s.sol`
* **Project Summary:** This project deploys a basic ERC-1155 multi-token standard contract. It includes functions for minting and burning tokens, with initial tokens minted during deployment.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (ERC1155, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To check the balance of a token ID for an address:
           `cast call 0xcaa53094C46e34Acb10D642377047c149ae87CE1 "balanceOf(address,uint256)(uint256)" YOUR_ADDRESS TOKEN_ID --rpc-url https://testnet-rpc.monad.xyz`
        4. To mint new tokens (only by owner):
           `cast send 0xcaa53094C46e34Acb10D642377047c149ae87CE1 "mint(address,uint256,uint256,bytes)" RECIPIENT_ADDRESS TOKEN_ID AMOUNT "0x" --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployMyERC1155Token.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key $PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/MyERC1155Token.sol -vvvv`
---
---
**Journal Entry: TimeLock (Basic Utility)**

* **Project Name:** TimeLock
* **Category:** Basic Utility
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 02, 2025 at 11:40:00 AM
* **GitHub Repository URL:** https://github.com/Huawei123r/my_first_monad_project
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x7e87758eC535318E7730fc7994A99Bd5c28Dc63d
* **Key Files Created:**
    * `contracts/TimeLock.sol`
    * `scripts/DeployTimeLock.s.sol`
* **Project Summary:** This project implements a time-locked wallet that allows users to deposit ETH or ERC-20 tokens, which can only be withdrawn after a specified unlock time. The owner can set the unlock time for any user.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To deposit ETH:
           `cast send 0x7e87758eC535318E7730fc7994A99Bd5c28Dc63d "deposit()" --value 1ether --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        4. To withdraw ETH (after lock time):
           `cast send 0x7e87758eC535318E7730fc7994A99Bd5c28Dc63d "withdraw()" --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        5. To set a new lock time for a user (only by owner):
           `cast send 0x7e87758eC535318E7730fc7994A99Bd5c28Dc63d "setLockTime(address,uint256)" USER_ADDRESS NEW_LOCK_TIMESTAMP --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployTimeLock.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key $PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/TimeLock.sol -vvvv`
---
---
**Journal Entry: Voting (Governance)**

* **Project Name:** Voting
* **Category:** Governance
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 02, 2025 at 11:50:00 AM
* **GitHub Repository URL:** https://github.com/Huawei123r/my_first_monad_project
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x3BCc94206A67D057Fd9ad66dCC928B795e58ed25
* **Key Files Created:**
    * `contracts/Voting.sol`
    * `scripts/DeployVoting.s.sol`
* **Project Summary:** This project implements a basic decentralized voting contract. The owner can create proposals, and users can vote on them. Each user can vote only once.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To create a proposal (only by owner):
           `cast send 0x3BCc94206A67D057Fd9ad66dCC928B795e58ed25 "createProposal(string)" "My First Proposal" --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        4. To vote on a proposal:
           `cast send 0x3BCc94206A67D057Fd9ad66dCC928B795e58ed25 "vote(uint256)" PROPOSAL_ID --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        5. To get proposal details:
           `cast call 0x3BCc94206A67D057Fd9ad66dCC928B795e58ed25 "getProposal(uint256)(uint256,string,uint256)" PROPOSAL_ID --rpc-url https://testnet-rpc.monad.xyz`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployVoting.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key $PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/Voting.sol -vvvv`
---
---
**Journal Entry: Crowdsale (Basic DeFi Protocol)**

* **Project Name:** Crowdsale
* **Category:** Basic DeFi Protocol
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 02, 2025 at 12:00:00 PM
* **GitHub Repository URL:** https://github.com/Huawei123r/my_first_monad_project
* **Monad Explorer Contract URL(s):** 
    * MyToken: https://testnet.monadexplorer.com/address/0x2109797f8B0c989Bb1D018C55749c386095189cc
    * Crowdsale: https://testnet.monadexplorer.com/address/0xd05d259573879953593F2dcf17493F7567cb6a38
* **Key Files Created:**
    * `contracts/Crowdsale.sol`
    * `scripts/DeployCrowdsale.s.sol`
* **Project Summary:** This project implements a basic crowdsale contract where users can purchase a custom ERC-20 token (MyCrowdsaleToken) with ETH. The crowdsale has a defined rate (tokens per ETH) and a cap on the total ETH raised. The ownership of the ERC-20 token is transferred to the Crowdsale contract upon deployment.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To buy tokens:
           `cast send 0xd05d259573879953593F2dcf17493F7567cb6a38 "buyTokens(address)" YOUR_ADDRESS --value 0.1ether --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        4. To withdraw funds (only by owner):
           `cast send 0xd05d259573879953593F2dcf17493F7567cb6a38 "withdrawFunds()" --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        5. To check the total supply of MyCrowdsaleToken:
           `cast call 0x2109797f8B0c989Bb1D018C55749c386095189cc "totalSupply()(uint256)" --rpc-url https://testnet-rpc.monad.xyz`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployCrowdsale.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key $PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/Crowdsale.sol -vvvv`
---
---
**Journal Entry: StakingRewards (Basic DeFi Protocol)**

* **Project Name:** StakingRewards
* **Category:** Basic DeFi Protocol
* **Network:** Monad Testnet
* **Deployment Timestamp:** July 02, 2025 at 12:10:00 PM
* **GitHub Repository URL:** https://github.com/Huawei123r/my_first_monad_project
* **Monad Explorer Contract URL(s):** 
    * StakingRewards: https://testnet.monadexplorer.com/address/0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd
    * MyFirstToken (Staking Token): https://testnet.monadexplorer.com/address/0xC7323a25F743dC6E63A78b5A3af5038E2810Eda4
    * SecondToken (Rewards Token): https://testnet.monadexplorer.com/address/0x412043B6ADfC627f8F8ACfEC9a996191B08AD4E8
* **Key Files Created:**
    * `contracts/StakingRewards.sol`
    * `scripts/DeployStakingRewards.s.sol`
* **Project Summary:** This project implements a basic staking rewards contract where users can stake a specific ERC-20 token (MyFirstToken) and earn rewards in another ERC-20 token (SecondToken). The contract owner can set the reward rate and distribute rewards.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (IERC20, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. Approve the StakingRewards contract to spend your staking tokens:
           `cast send STAKING_TOKEN_ADDRESS "approve(address,uint256)" STAKING_REWARDS_CONTRACT_ADDRESS AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        4. To stake tokens:
           `cast send 0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd "stake(uint256)" AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        5. To withdraw staked tokens:
           `cast send 0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd "withdraw(uint256)" AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        6. To get rewards:
           `cast send 0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd "getReward()" --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        7. To set reward rate (only by owner):
           `cast send 0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd "setRewardRate(uint256)" RATE --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
        8. To distribute rewards (only by owner):
           `cast send REWARDS_TOKEN_ADDRESS "approve(address,uint256)" STAKING_REWARDS_CONTRACT_ADDRESS AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
           `cast send 0xF7E4616A75BD80a72D3cE5FA32E61471a30161cd "distributeRewards(uint256)" AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployStakingRewards.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key $PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/StakingRewards.sol -vvvv`
---