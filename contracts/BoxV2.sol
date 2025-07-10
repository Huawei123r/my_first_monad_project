// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./Box.sol";

contract BoxV2 is Box {
    function increment() public {
        _value = _value + 1;
    }
}
