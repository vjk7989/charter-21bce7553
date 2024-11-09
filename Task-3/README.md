# Signature Verification System

A robust web application built with Streamlit for verifying digital signatures using ECDSA and Schnorr signature schemes. This system provides an intuitive interface for signature verification and demo data generation.

## 🌟 Features

- **Multiple Signature Schemes Support**
  - ECDSA (Elliptic Curve Digital Signature Algorithm)
  - Schnorr Signatures (placeholder implementation)
  - RSA (planned)

- **Smart Features**
  - Automatic signature scheme detection
  - Real-time signature validation
  - Performance metrics display
  - Interactive demo data generation
  - Component-wise signature analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   # Using HTTPS
   git clone https://github.com/yourusername/signature-verification-system.git

   # OR using SSH
   git clone git@github.com:yourusername/signature-verification-system.git

   # Navigate to project directory
   cd signature-verification-system
   ```

2. **Set up a virtual environment**

   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate

   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit server**
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

## 💻 Usage

### Verifying Signatures

1. Navigate to the "Verify Signature" tab
2. Choose a signature scheme (or use Auto Detect)
3. Enter the original message
4. Paste the signature in hexadecimal format
5. Click "Verify Signature"

### Generating Demo Data

1. Go to the "Generate Demo Data" tab
2. Click "Generate Demo Data"
3. Use the generated data to test the verification system
4. Follow the provided instructions to verify the demo signature

## 🔧 Technical Details

### Supported Signature Schemes

- **ECDSA**
  - 65-byte signatures (r: 32 bytes, s: 32 bytes, v: 1 byte)
  - Uses SECP256k1 curve
  - Full implementation with public key recovery

- **Schnorr**
  - 64-byte signatures (r: 32 bytes, s: 32 bytes)
  - Uses SECP256k1 curve
  - Placeholder implementation

## 📁 Project Structure

```plaintext
signature-verification-system/
├── main.py              # Main application file
├── requirements.txt     # Project dependencies
├── venv/               # Virtual environment
└── README.md           # Documentation
```

## ⚙️ Dependencies

```plaintext
streamlit      # Web application framework
ecdsa==0.18.0  # Elliptic Curve Digital Signature Algorithm
```

## 📝 Code Snippets

### Main Application (main.py)

```python
def main():
    st.set_page_config(
        page_title="Signature Verifier",
        page_icon="🔐",
        layout="wide"
    )
    
    st.title("🔐 Signature Verifier")
    
    tab1, tab2 = st.tabs(["Verify Signature", "Generate Demo Data"])
    
    # ... rest of the main function code ...
```

### Requirements (requirements.txt)

```plaintext
streamlit
ecdsa==0.18.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- Implementation of full Schnorr signature verification
- Addition of RSA signature support
- Batch verification capabilities
- Support for custom curves and parameters
- Enhanced error reporting and debugging tools

## ⚠️ Security Notice

This system is intended for educational and testing purposes. For production use, please ensure proper security auditing and hardening.

## 🐛 Known Issues

- Schnorr signature verification is currently a placeholder
- RSA implementation pending
- Limited error handling in some edge cases

## 📋 Development Notes

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_signature_verifier.py
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document all public methods
- Keep functions focused and small

## 🔍 Troubleshooting

### Common Issues

1. **Installation Problems**
   ```bash
   # If you encounter SSL errors
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
   ```

2. **Signature Verification Fails**
   - Ensure correct signature format
   - Verify message encoding
   - Check signature scheme selection


## 🙏 Acknowledgments

- ECDSA library developers
- Streamlit community
- All contributors

---

*Last updated: [Current Date]*
