const { ethers } = require("hardhat");

async function main() {
  const [deployer, beneficiary] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const Escrow = await ethers.getContractFactory("Escrow");
  const escrow = await Escrow.deploy(beneficiary.address, {
    value: ethers.parseEther("1.0")
  });

  await escrow.waitForDeployment();

  console.log("Escrow deployed to:", await escrow.getAddress());
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
