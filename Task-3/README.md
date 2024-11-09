# Signature Verifier

This project provides a tool to verify cryptographic signatures using various signature schemes, including ECDSA and a placeholder for Schnorr signatures. It allows users to verify signatures, check their validity, and also generate demo data for testing.

## Features

- Supports **ECDSA** (Elliptic Curve Digital Signature Algorithm) signatures
- Placeholder for **Schnorr** signatures
- Auto-detects the signature scheme
- Validates components of the signature (r, s, v)
- Demo data generation for testing
- Time efficiency metrics for verification
- User-friendly interface with Streamlit

## Requirements

- Python 3.7+
- Required Python libraries (`streamlit`, `ecdsa`, etc.)

## Setting Up the Project

### Step 1: Set Up a Virtual Environment

First, create a virtual environment to manage dependencies.

1. Navigate to the directory where you want to store the project files.
   
2. Run the following command to create a virtual environment:

   ```bash
   python3 -m venv venv
   ```
