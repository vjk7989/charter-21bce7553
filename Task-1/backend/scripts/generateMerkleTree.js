const { MerkleTree } = require('merkletreejs');
const keccak256 = require('keccak256');
const fs = require('fs');

// Generate 10 random transactions
function generateRandomTransactions(count) {
    const transactions = [];
    for (let i = 0; i < count; i++) {
        // Generate a random 32-byte hex string
        const tx = '0x' + [...Array(64)].map(() => Math.floor(Math.random() * 16).toString(16)).join('');
        transactions.push(tx);
    }
    return transactions;
}

async function main() {
    try {
        // Generate random transactions
        const transactions = generateRandomTransactions(10);

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

        // Save to JSON file
        const data = {
            merkleRoot: root,
            transactions: merkleData
        };

        fs.writeFileSync(
            'merkle-data.json',
            JSON.stringify(data, null, 2)
        );

        console.log("Merkle tree data generated and saved to merkle-data.json");
        console.log("Merkle Root:", root);
        console.log("\nSample transaction data:");
        console.log(merkleData[0]);

    } catch (error) {
        console.error("Generation failed:", error);
        throw error;
    }
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
}); 