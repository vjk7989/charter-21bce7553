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
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source venv/bin/activate
On Windows:

bash
Copy code
venv\Scripts\activate
Step 2: Install Dependencies
Make sure the virtual environment is activated (you should see (venv) at the beginning of your terminal prompt).

Install the required dependencies by running:

bash
Copy code
pip install -r requirements.txt
Step 3: Create requirements.txt
If you don't have a requirements.txt, create one by running:

bash
Copy code
pip freeze > requirements.txt
Ensure that requirements.txt contains the following:

txt
Copy code
streamlit==1.24.0
ecdsa==0.18.0
Step 4: Running the Application
To run the app, use the following command while the virtual environment is active:

bash
Copy code
streamlit run main.py
This will start the Streamlit app and open a browser window with the interface for verifying signatures and generating demo data.

Step 5: Usage
Verify Signature Tab:

Input a message, paste the signature in hexadecimal format, and select the signature scheme or let the system auto-detect.
Click "Verify Signature" to see if the signature is valid or not.
Generate Demo Data Tab:

Click "Generate Demo Data" to generate a demo message, signature, and its components (r, s, v).
Use the generated data to test the signature verification.
Step 6: Stopping the Application
To stop the application, simply press Ctrl+C in your terminal.

Optional: Deactivating the Virtual Environment
Once you are done, deactivate the virtual environment by running:

bash
Copy code
deactivate
About the Code
This project uses the ecdsa library to implement ECDSA verification. It also has placeholders for verifying Schnorr signatures (you can implement that logic later).

The project is built using Streamlit for the user interface, which makes it easy to build and deploy interactive data apps.

Signature Schemes Supported:
ECDSA: An elliptic curve-based algorithm for digital signatures.
Schnorr: A signature scheme that is currently not implemented but can be added.
