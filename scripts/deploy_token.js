const hre = require("hardhat");

async function main() {
  const MyFirstToken = await hre.ethers.getContractFactory("MyFirstToken");
  const myFirstToken = await MyFirstToken.deploy(await (await hre.ethers.getSigners())[0].getAddress());

  await myFirstToken.deployed();

  console.log("MyFirstToken deployed to:", myFirstToken.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
