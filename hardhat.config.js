require("@nomicfoundation/hardhat-toolbox");
require('@openzeppelin/hardhat-upgrades');

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.20",
  networks: {
    monad: {
      url: "https://testnet-rpc.monad.xyz/",
      accounts: ["0x75e877ba5d5b6c665dab973b7d1278bd5c530dd36ba80eac23ca37fd5fcbdcfb"]
    }
  }
};
