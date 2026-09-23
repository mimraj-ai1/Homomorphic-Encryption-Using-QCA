"""
End-to-End Homomorphic Computation Demonstration and Verification Suite.

Demonstrates:
1. Paillier Additive Homomorphism:
   - Keypair generation (Public Key: n, g; Private Key: lambda, mu)
   - Plaintext encryption
   - Ciphertext-domain addition: c_sum = c1 * c2 mod n^2
   - Verification: Decrypt(c_sum) == (m1 + m2) mod n
   - Ciphertext-domain scalar multiplication: c_scale = c1^k mod n^2
   - Verification: Decrypt(c_scale) == (k * m1) mod n
   - Ciphertext-domain subtraction: c_diff = c2 * c1^-1 mod n^2
   - Verification: Decrypt(c_diff) == (m2 - m1) mod n
2. Multiplicative Homomorphism (RSA):
   - Keypair generation
   - Ciphertext-domain multiplication: c_prod = c1 * c2 mod N
   - Verification: Decrypt(c_prod) == (m1 * m2) mod N
3. Architectural Hardware Mapping:
   - Maps modular arithmetic operations to physical QCA circuit modules
"""

import sys
from encryption import generate_paillier_keypair, generate_rsa_keypair
from operations import (
    paillier_add,
    paillier_multiply_scalar,
    paillier_subtract,
    rsa_multiply,
    trace_hardware_decomposition,
)


def run_demonstration():
    print("=" * 75)
    print("HOMOMORPHIC ENCRYPTION (HE) SOFTWARE DEMONSTRATION")
    print("=" * 75)

    # -------------------------------------------------------------------------
    # PART 1: PAILLIER ADDITIVE HOMOMORPHISM
    # -------------------------------------------------------------------------
    print("\n[PART 1: Paillier Additive Homomorphism]")
    print("-" * 75)

    print("Generating 64-bit Paillier Keypair...")
    pubkey, privkey = generate_paillier_keypair(bits=64)
    print(f"  Public Modulus n      : {pubkey.n} ({pubkey.n.bit_length()} bits)")
    print(f"  Public Modulus n^2    : {pubkey.n_sq}")
    print(f"  Public Generator g    : {pubkey.g}")
    print(f"  Private Lambda        : {privkey.lam}")
    print(f"  Private Mu            : {privkey.mu}")

    # Plaintexts
    m1 = 15
    m2 = 27
    print(f"\nPlaintext Operands:")
    print(f"  m1 = {m1}")
    print(f"  m2 = {m2}")

    # Encryption
    c1 = pubkey.encrypt(m1)
    c2 = pubkey.encrypt(m2)
    print(f"\nEncrypted Ciphertexts (in Z_n^2*):")
    print(f"  c1 = E({m1}) = {hex(c1)}")
    print(f"  c2 = E({m2}) = {hex(c2)}")

    # 1. Homomorphic Addition
    c_add = paillier_add(pubkey, c1, c2)
    decrypted_add = privkey.decrypt(c_add)
    expected_add = (m1 + m2) % pubkey.n
    print(f"\n1. Homomorphic Addition: c_add = (c1 * c2) mod n^2")
    print(f"  c_add                  = {hex(c_add)}")
    print(f"  Decrypted Result       = {decrypted_add}")
    print(f"  Expected Plaintext Sum = {expected_add}")
    assert decrypted_add == expected_add, "Paillier addition verification failed!"
    print(f"  --> VERIFICATION STATUS: PASSED (Match: {decrypted_add} == {expected_add})")

    # 2. Homomorphic Scalar Multiplication
    scalar_k = 5
    c_scale = paillier_multiply_scalar(pubkey, c1, scalar_k)
    decrypted_scale = privkey.decrypt(c_scale)
    expected_scale = (scalar_k * m1) % pubkey.n
    print(f"\n2. Homomorphic Scalar Multiplication: c_scale = (c1 ^ {scalar_k}) mod n^2")
    print(f"  c_scale                = {hex(c_scale)}")
    print(f"  Decrypted Result       = {decrypted_scale}")
    print(f"  Expected Plaintext Mul = {expected_scale}")
    assert decrypted_scale == expected_scale, "Paillier scalar multiplication failed!"
    print(f"  --> VERIFICATION STATUS: PASSED (Match: {decrypted_scale} == {expected_scale})")

    # 3. Homomorphic Subtraction
    c_sub = paillier_subtract(pubkey, c2, c1)
    decrypted_sub = privkey.decrypt(c_sub)
    expected_sub = (m2 - m1) % pubkey.n
    print(f"\n3. Homomorphic Subtraction: c_sub = (c2 * c1^-1) mod n^2")
    print(f"  c_sub                  = {hex(c_sub)}")
    print(f"  Decrypted Result       = {decrypted_sub}")
    print(f"  Expected Plaintext Sub = {expected_sub}")
    assert decrypted_sub == expected_sub, "Paillier subtraction failed!"
    print(f"  --> VERIFICATION STATUS: PASSED (Match: {decrypted_sub} == {expected_sub})")

    # -------------------------------------------------------------------------
    # PART 2: MULTIPLICATIVE HOMOMORPHISM (UNPADDED RSA)
    # -------------------------------------------------------------------------
    print("\n[PART 2: Multiplicative Homomorphism (RSA)]")
    print("-" * 75)

    print("Generating 64-bit RSA Keypair...")
    rsa_pub, rsa_priv = generate_rsa_keypair(bits=64)
    print(f"  RSA Modulus N         : {rsa_pub.n}")
    print(f"  Public Exponent e     : {rsa_pub.e}")
    print(f"  Private Exponent d    : {rsa_priv.d}")

    m_a = 7
    m_b = 6
    c_a = rsa_pub.encrypt(m_a)
    c_b = rsa_pub.encrypt(m_b)
    print(f"\nPlaintext Operands: m_a = {m_a}, m_b = {m_b}")
    print(f"  c_a = {hex(c_a)}")
    print(f"  c_b = {hex(c_b)}")

    c_prod = rsa_multiply(rsa_pub, c_a, c_b)
    decrypted_prod = rsa_priv.decrypt(c_prod)
    expected_prod = (m_a * m_b) % rsa_pub.n
    print(f"\nHomomorphic Multiplication: c_prod = (c_a * c_b) mod N")
    print(f"  c_prod                 = {hex(c_prod)}")
    print(f"  Decrypted Result       = {decrypted_prod}")
    print(f"  Expected Plaintext Mul = {expected_prod}")
    assert decrypted_prod == expected_prod, "RSA multiplication verification failed!"
    print(f"  --> VERIFICATION STATUS: PASSED (Match: {decrypted_prod} == {expected_prod})")

    # -------------------------------------------------------------------------
    # PART 3: ARCHITECTURAL HARDWARE DECOMPOSITION TO QCA
    # -------------------------------------------------------------------------
    print("\n[PART 3: Architectural Hardware Mapping to QCA Modules]")
    print("-" * 75)
    decomp = trace_hardware_decomposition(operand_a=m1, operand_b=m2, word_size_bits=4)
    print(f"Decomposing 4-bit Arithmetic Slice (A={decomp['operand_a_word']}, B={decomp['operand_b_word']}):")
    print(f"  1. 2-bit Slices Partial Product Evaluation:")
    for pp in decomp["partial_products_2x2"]:
        print(f"     - Slice ({pp['slice_a']} * {pp['slice_b']}) = {pp['product']} (Weight 2^{pp['bit_weight']})")
    print(f"  2. Integer Sum Accumulation:")
    print(f"     - A + B = {decomp['integer_sum']}")
    print(f"  3. Modulo-4 Residue Reduction:")
    print(f"     - (A + B) mod 4 = {decomp['mod_4_residue']} (Residue Bits: R1={decomp['mod_4_residue']>>1}, R0={decomp['mod_4_residue']&1})")
    print(f"     - Overflow Quotient Q = {decomp['mod_4_overflow']}")
    print(f"\nPhysical QCA Layout Mapping:")
    for role, qca_circ in decomp["qca_modules_required"].items():
        print(f"  - {role:<32}: {qca_circ}")

    print("\n" + "=" * 75)
    print("ALL HOMOMORPHIC ENCRYPTION VERIFICATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 75)


if __name__ == "__main__":
    run_demonstration()
