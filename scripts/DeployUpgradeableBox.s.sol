// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Script} from "forge-std/Script.sol";
import {Box} from "../contracts/Box.sol";
import {UUPSUpgradeable} from "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

contract DeployUpgradeableBox is Script {
    function run() public returns (Box, ERC1967Proxy) {
        vm.startBroadcast();

        // Deploy the implementation contract
        Box boxImplementation = new Box();

        // Deploy the proxy, pointing to the implementation
        // The initializer function is called through the proxy
        bytes memory initializeData = abi.encodeWithSelector(boxImplementation.initialize.selector, 100);
        ERC1967Proxy boxProxy = new ERC1967Proxy(address(boxImplementation), initializeData);

        vm.stopBroadcast();

        return (Box(address(boxProxy)), boxProxy);
    }
}
