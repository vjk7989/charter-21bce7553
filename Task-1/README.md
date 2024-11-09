MERKLE PROOF VERIFICATION SYSTEM
===============================

A blockchain-based system for verifying transactions using Merkle trees. (backend part only)

CONTENTS
--------
1. Overview
2. Setup
3. Contract Details
4. Scripts
5. Testing
6. Troubleshooting

1. OVERVIEW
-----------
This system implements Merkle tree-based transaction verification using:
- Hardhat development environment
- Solidity smart contracts
- OpenZeppelin libraries
- MerkleTree.js for proof generation

2. SETUP
--------
Prerequisites:
- Node.js (v14+)
- npm/yarn
- MetaMask wallet
- Sepolia testnet ETH

Installation Steps:
1. Clone repository
2. Run: npm install
3. Create .env file with:
   SEPOLIA_RPC_URL=your_sepolia_rpc_url
   PRIVATE_KEY=your_wallet_private_key
4. npx hardhat run scripts/deploy.js    

Getting Test ETH:
- Sepolia Faucet (sepoliafaucet.com)
- Infura Faucet (infura.io/faucet/sepolia)
- QuickNode Faucet (faucet.quicknode.com/ethereum/sepolia)

3. CONTRACT DETAILS
------------------
MerkleProofVerifier.sol:
- Manages Merkle root storage
- Verifies transaction proofs
- Inherits OpenZeppelin's Ownable
- Uses MerkleProof library

Key Functions:
- setMerkleRoot(): Set the Merkle root (owner only)
- verifyTransaction(): Verify transaction inclusion

4. SCRIPTS
----------
generateMerkleTree.js:
- Generates random transactions
- Creates Merkle tree
- Saves proofs to merkle-data.json

deploy.js:
- Deploys MerkleProofVerifier contract
- Sets initial Merkle root
- Saves deployment data

5. TESTING
----------
Commands:
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Lock.js

6. TROUBLESHOOTING
-----------------
Common Issues:

1. Insufficient Balance
   Error: "Insufficient SepoliaETH"
   Fix: Get ETH from faucets

2. RPC Errors
   Error: "Cannot connect to RPC"
   Fix: Check .env configuration

3. Deployment Failures
   Error: "Cannot estimate gas"
   Fix: Ensure sufficient ETH balance

DEPENDENCIES
-----------
Core:
- @openzeppelin/contracts: ^5.1.0
- merkletreejs: ^0.4.0
- keccak256: ^1.0.6
- hardhat: ^2.22.15
- dotenv: ^16.4.5

Development:
- @nomicfoundation/hardhat-toolbox: ^5.0.0

CONFIGURATION
------------
Hardhat Settings:
- Solidity: 0.8.27
- Optimizer: enabled (200 runs)
- Network: Sepolia testnet

FILE STRUCTURE
-------------
backend/
├── contracts/
│   ├── MerkleProofVerifier.sol
│   └── Lock.sol
├── scripts/
│   ├── deploy.js
│   └── generateMerkleTree.js
├── test/
│   └── Lock.js
├── hardhat.config.js
└── package.json

SECURITY NOTES
-------------
1. Never commit .env file
2. Keep private keys secure
3. Use separate deployment accounts
4. Verify contract source code
5. Test thoroughly before mainnet deployment

SUPPORT
-------
For issues:
1. Check troubleshooting section
2. Review logs
3. Open GitHub issue
4. Contact development team

LICENSE
-------
UNLICENSED

[END OF FILE]



