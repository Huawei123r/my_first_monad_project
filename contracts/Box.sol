// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";

contract Box is UUPSUpgradeable, OwnableUpgradeable {
    uint256 private _value;

    event ValueChanged(uint256 newValue);

    function initialize(uint256 value) initializer public {
        __Ownable_init(msg.sender);
        __UUPSUpgradeable_init();
        _value = value;
    }

    function store(uint256 value) public onlyOwner {
        _value = value;
        emit ValueChanged(value);
    }

    function retrieve() public view returns (uint256) {
        return _value;
    }

    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}
}