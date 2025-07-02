// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Script} from "forge-std/Script.sol";
import {StakingRewards} from "../contracts/StakingRewards.sol";
import {MyFirstToken} from "../contracts/MyFirstToken.sol";
import {SecondToken} from "../contracts/SecondToken.sol";

contract DeployStakingRewards is Script {
    function run() public returns (StakingRewards, MyFirstToken, SecondToken) {
        vm.startBroadcast();

        // Deploy Staking Token with an initial supply
        MyFirstToken stakingToken = new MyFirstToken(1000000 * 10 ** 18); // 1,000,000 tokens

        // Deploy Rewards Token with an initial supply
        SecondToken rewardsToken = new SecondToken(1000000 * 10 ** 18); // 1,000,000 tokens

        // Deploy StakingRewards contract
        StakingRewards stakingRewards = new StakingRewards(address(stakingToken), address(rewardsToken));

        vm.stopBroadcast();

        return (stakingRewards, stakingToken, rewardsToken);
    }
}