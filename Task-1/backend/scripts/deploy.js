const hre = require("hardhat");
const { MerkleTree } = require('merkletreejs');
const keccak256 = require('keccak256');
const fs = require('fs');

// Sample transaction data - replace with your actual data
const transactions = [
  "0x1234...",
  "0x5678...",
  // Add more transactions
];

async function main() {
  try {
    // Create Merkle Tree
    const leaves = transactions.map(tx => keccak256(tx));
    const tree = new MerkleTree(leaves, keccak256, { sortPairs: true });
    const root = tree.getHexRoot();

    // Generate proofs for each transaction
    const merkleData = transactions.map(tx => {
      const leaf = keccak256(tx);
      const proof = tree.getHexProof(leaf);
      return {
        transaction: tx,
        leaf: '0x' + leaf.toString('hex'),
        proof: proof
      };
    });

    // Deploy contract
    const [deployer] = await hre.ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);
    
    const balance = await hre.ethers.provider.getBalance(deployer.address);
    console.log("Account balance:", hre.ethers.formatEther(balance), "SepoliaETH");

    if (balance < hre.ethers.parseEther("0.01")) {
      console.error("\nError: Insufficient SepoliaETH. You need at least 0.01 SepoliaETH.");
      process.exit(1);
    }

    const MerkleProofVerifier = await hre.ethers.getContractFactory("MerkleProofVerifier");
    console.log("Deploying contract...");
    
    const verifier = await MerkleProofVerifier.deploy();
    await verifier.waitForDeployment();
    
    const address = await verifier.getAddress();
    console.log("MerkleProofVerifier deployed to:", address);

    // Set the Merkle root
    const setRootTx = await verifier.setMerkleRoot(root);
    await setRootTx.wait();
    console.log("Merkle root set:", root);

    // Save deployment data
    const deployData = {
      contractAddress: address,
      merkleRoot: root,
      transactions: merkleData
    };

    fs.writeFileSync(
      'deployment-data.json',
      JSON.stringify(deployData, null, 2)
    );

    console.log("Deployment data saved to deployment-data.json");

  } catch (error) {
    console.error("Deployment failed:", error);
    throw error;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
