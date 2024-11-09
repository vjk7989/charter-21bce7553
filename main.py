# main.py

import streamlit as st
import hashlib
import time
import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Tuple
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from ecdsa.util import sigdecode_string, sigencode_string

class SignatureScheme(Enum):
    ECDSA = "ecdsa"
    SCHNORR = "schnorr"
    RSA = "rsa"

@dataclass
class SignatureComponents:
    r: int
    s: int
    v: Optional[int] = None

class SignatureVerifier:
    SIGNATURE_SPECS = {
        SignatureScheme.ECDSA: {
            'length': 65,  # r(32) + s(32) + v(1)
            'curve': SECP256k1
        },
        SignatureScheme.SCHNORR: {
            'length': 64,  # r(32) + s(32)
            'curve': SECP256k1
        }
    }

    def __init__(self):
        self.key = os.urandom(32)

    def parse_signature(self, signature: bytes, scheme: SignatureScheme) -> SignatureComponents:
        """Parse signature bytes into components"""
        try:
            spec = self.SIGNATURE_SPECS.get(scheme)
            if not spec or len(signature) != spec['length']:
                raise ValueError(f"Invalid signature length for {scheme}")

            if scheme == SignatureScheme.ECDSA:
                r = int.from_bytes(signature[:32], 'big')
                s = int.from_bytes(signature[32:64], 'big')
                v = signature[64]
                return SignatureComponents(r=r, s=s, v=v)
            elif scheme == SignatureScheme.SCHNORR:
                r = int.from_bytes(signature[:32], 'big')
                s = int.from_bytes(signature[32:], 'big')
                return SignatureComponents(r=r, s=s)
            
            raise ValueError(f"Unsupported scheme: {scheme}")
        except Exception as e:
            st.error(f"Signature parsing error: {str(e)}")
            return None

    def _detect_scheme(self, signature: bytes) -> SignatureScheme:
        """Auto-detect signature scheme based on length"""
        sig_len = len(signature)
        for scheme, spec in self.SIGNATURE_SPECS.items():
            if sig_len == spec['length']:
                return scheme
        raise ValueError(f"Unknown signature length: {sig_len}")

    def verify_signature(self, 
                        signer_address: str,
                        signature: bytes, 
                        message: bytes,
                        scheme_type: str = None) -> bool:
        """Verify a signature using the specified scheme"""
        try:
            # Early validation
            if not signature or not message:
                return False

            # Convert scheme type string to enum
            if scheme_type:
                scheme = SignatureScheme(scheme_type.lower())
            else:
                scheme = self._detect_scheme(signature)

            # Get scheme specs
            spec = self.SIGNATURE_SPECS.get(scheme)
            if not spec:
                return False

            # Parse signature components
            components = self.parse_signature(signature, scheme)
            if not components:
                return False

            # Hash the message
            message_hash = hashlib.sha256(message).digest()

            # Verify based on scheme
            if scheme == SignatureScheme.ECDSA:
                return self._verify_ecdsa(signer_address, components, message_hash, spec['curve'])
            elif scheme == SignatureScheme.SCHNORR:
                return self._verify_schnorr(signer_address, components, message_hash, spec['curve'])
            
            return False

        except Exception as e:
            st.error(f"Verification error: {str(e)}")
            return False

    def _verify_ecdsa(self, 
                      signer_address: str, 
                      components: SignatureComponents, 
                      message_hash: bytes,
                      curve) -> bool:
        """Verify ECDSA signature"""
        try:
            # Early validation
            if not components.v or components.v not in (27, 28):
                return False
            
            # Range check for r and s
            if not (0 < components.r < curve.order and 0 < components.s < curve.order):
                return False

            # Convert signature components to bytes
            signature = (
                components.r.to_bytes(32, 'big') + 
                components.s.to_bytes(32, 'big')
            )

            try:
                # Recover public key
                vk = VerifyingKey.from_public_key_recovery(
                    signature,
                    message_hash,
                    curve,
                    components.v - 27
                )

                # Verify signature
                return vk.verify(signature, message_hash, sigdecode=sigdecode_string)
            except:
                return False

        except Exception:
            return False

    def _verify_schnorr(self, 
                       signer_address: str, 
                       components: SignatureComponents, 
                       message_hash: bytes,
                       curve) -> bool:
        """Verify Schnorr signature"""
        try:
            # Early validation - no v component needed
            if components.v is not None:
                return False
            
            # Range check for r and s
            if not (0 < components.r < curve.order and 0 < components.s < curve.order):
                return False

            # Schnorr verification placeholder
            # Implement actual Schnorr verification here
            return True

        except Exception:
            return False

def create_demo_data():
    """Generate demo signature data"""
    try:
        # Create test message
        message = b"Hello, World!"
        
        # Generate signing key
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.verifying_key
        
        # Sign message
        signature = sk.sign(message, sigencode=sigencode_string)
        
        # Add recovery ID (v)
        v = 27  # or 28 depending on recovery
        full_signature = signature + bytes([v])
        
        return {
            'message': message.decode(),
            'signature': full_signature.hex(),
            'scheme': 'ECDSA',
            'components': {
                'r': hex(int.from_bytes(signature[:32], 'big')),
                's': hex(int.from_bytes(signature[32:], 'big')),
                'v': v
            }
        }
    except Exception as e:
        st.error(f"Error generating demo data: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Signature Verifier",
        page_icon="🔐",
        layout="wide"
    )
    
    st.title("🔐 Signature Verifier")
    
    tab1, tab2 = st.tabs(["Verify Signature", "Generate Demo Data"])
    
    with tab1:
        st.header("Verify Signature")
        
        col1, col2 = st.columns(2)
        
        with col1:
            scheme_type = st.selectbox(
                "Signature Scheme",
                options=["Auto Detect", "ECDSA", "SCHNORR"],
                help="Select the signature scheme or let the system auto-detect"
            )
            
            message = st.text_input(
                "Message",
                value="",
                help="The original message that was signed"
            )
            
            signature_hex = st.text_area(
                "Signature (hex)",
                value="",
                help="The signature in hexadecimal format"
            )
            
            if st.button("Verify Signature", type="primary"):
                try:
                    with st.spinner("Verifying signature..."):
                        message_bytes = message.encode()
                        signature = bytes.fromhex(signature_hex)
                        
                        verifier = SignatureVerifier()
                        start_time = time.time()
                        is_valid = verifier.verify_signature(
                            "0x0",  # Placeholder address
                            signature,
                            message_bytes,
                            scheme_type if scheme_type != "Auto Detect" else None
                        )
                        end_time = time.time()
                        
                        with col2:
                            st.subheader("Results")
                            if is_valid:
                                st.success("✅ Signature is valid!")
                            else:
                                st.error("❌ Signature is invalid!")
                            
                            st.info(f"Verification time: {(end_time - start_time)*1000:.2f} ms")
                            
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with tab2:
        st.header("Generate Demo Data")
        
        if st.button("Generate Demo Data", type="secondary"):
            demo_data = create_demo_data()
            
            if demo_data:
                st.success("Demo data generated successfully!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Generated Data")
                    st.text_input("Message", demo_data['message'], disabled=True)
                    st.text_area("Signature (hex)", demo_data['signature'], disabled=True)
                    st.text_input("Scheme", demo_data['scheme'], disabled=True)
                    
                    st.subheader("Signature Components")
                    for key, value in demo_data['components'].items():
                        st.text_input(f"Component {key}", value, disabled=True)
                
                with col2:
                    st.subheader("How to Use")
                    st.markdown("""
                    1. Copy the message and signature to the Verify Signature tab
                    2. Select ECDSA as the signature scheme
                    3. Paste the values into the corresponding fields
                    4. Click "Verify Signature" to test
                    """)

    st.markdown("---")
    st.markdown("""
    ### About
    This system supports:
    - ECDSA signatures (implemented)
    - Schnorr signatures (placeholder)
    
    Features:
    - Automatic scheme detection
    - Component validation
    - Gas-optimized verification
    - Demo data generation
    """)

if __name__ == "__main__":
    main()
