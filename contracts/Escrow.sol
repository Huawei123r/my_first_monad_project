// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Escrow {
    address public depositor;
    address public beneficiary;
    uint256 public amount;

    constructor(address _beneficiary) payable {
        depositor = msg.sender;
        beneficiary = _beneficiary;
        amount = msg.value;
    }

    function release() public {
        require(msg.sender == beneficiary, "Only the beneficiary can release the funds.");
        payable(beneficiary).transfer(amount);
    }
}
