"""
Comprehensive Unit Tests for Homomorphic Encryption (HE) Demonstration.
Tests:
1. Mathematical primitives (gcd, lcm, mod_inverse, Miller-Rabin primality).
2. Paillier Key Generation, Encryption, and Decryption roundtrip.
3. Paillier Homomorphic Addition: Decrypt(c1 * c2 mod n^2) == (m1 + m2) mod n.
4. Paillier Homomorphic Addition with Plaintext Constant: Decrypt(c * g^k mod n^2) == (m + k) mod n.
5. Paillier Homomorphic Scalar Multiplication: Decrypt(c^k mod n^2) == (k * m) mod n.
6. Paillier Homomorphic Subtraction: Decrypt(c2 * c1^-1 mod n^2) == (m2 - m1) mod n.
7. RSA Multiplicative Homomorphism: Decrypt(c1 * c2 mod N) == (m1 * m2) mod N.
8. Hardware Decomposition and QCA Layout Mapping.
"""

import os
import sys
import pytest

# Ensure HE_Demo is in Python search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "HE_Demo")))

from encryption import (
    gcd,
    lcm,
    mod_inverse,
    is_prime,
    generate_prime,
    generate_paillier_keypair,
    generate_rsa_keypair,
    PaillierPublicKey,
    PaillierPrivateKey,
    RSAPublicKey,
    RSAPrivateKey,
)
from operations import (
    paillier_add,
    paillier_add_plain,
    paillier_multiply_scalar,
    paillier_subtract,
    rsa_multiply,
    trace_hardware_decomposition,
)


class TestCryptographicPrimitives:
    def test_gcd_lcm(self):
        assert gcd(54, 24) == 6
        assert lcm(4, 6) == 12
        assert gcd(17, 31) == 1
        assert lcm(17, 31) == 527

    def test_modular_inverse(self):
        inv = mod_inverse(3, 11)
        assert (3 * inv) % 11 == 1
        inv2 = mod_inverse(17, 3120)
        assert (17 * inv2) % 3120 == 1

    def test_primality_test(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        for p in primes:
            assert is_prime(p), f"Failed for known prime: {p}"
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 25, 27, 33, 35, 49, 77, 91]
        for c in composites:
            assert not is_prime(c), f"Failed for known composite: {c}"

    def test_prime_generator(self):
        p = generate_prime(bits=32)
        assert p.bit_length() == 32
        assert is_prime(p)


class TestPaillierHomomorphism:
    @pytest.fixture(scope="class")
    def paillier_keys(self):
        # 48-bit keypair for fast, deterministic unit test execution
        pub, priv = generate_paillier_keypair(bits=48)
        return pub, priv

    def test_encryption_decryption_roundtrip(self, paillier_keys):
        pub, priv = paillier_keys
        messages = [0, 1, 42, 100, 255, 1024]
        for m in messages:
            c = pub.encrypt(m)
            decrypted = priv.decrypt(c)
            assert decrypted == m, f"Roundtrip failed for message {m}"

    @pytest.mark.parametrize("m1, m2", [(10, 20), (0, 45), (100, 250), (999, 1)])
    def test_homomorphic_addition(self, paillier_keys, m1, m2):
        pub, priv = paillier_keys
        c1 = pub.encrypt(m1)
        c2 = pub.encrypt(m2)

        c_sum = paillier_add(pub, c1, c2)
        decrypted_sum = priv.decrypt(c_sum)
        expected_sum = (m1 + m2) % pub.n

        assert decrypted_sum == expected_sum

    @pytest.mark.parametrize("m, plain_const", [(15, 25), (0, 7), (120, 80)])
    def test_homomorphic_addition_plaintext(self, paillier_keys, m, plain_const):
        pub, priv = paillier_keys
        c = pub.encrypt(m)

        c_res = paillier_add_plain(pub, c, plain_const)
        decrypted = priv.decrypt(c_res)
        expected = (m + plain_const) % pub.n

        assert decrypted == expected

    @pytest.mark.parametrize("m, k", [(7, 3), (12, 5), (4, 10), (0, 8)])
    def test_homomorphic_scalar_multiplication(self, paillier_keys, m, k):
        pub, priv = paillier_keys
        c = pub.encrypt(m)

        c_prod = paillier_multiply_scalar(pub, c, k)
        decrypted = priv.decrypt(c_prod)
        expected = (k * m) % pub.n

        assert decrypted == expected

    @pytest.mark.parametrize("m1, m2", [(50, 20), (100, 100), (350, 120)])
    def test_homomorphic_subtraction(self, paillier_keys, m1, m2):
        pub, priv = paillier_keys
        c1 = pub.encrypt(m1)
        c2 = pub.encrypt(m2)

        c_diff = paillier_subtract(pub, c1, c2)
        decrypted = priv.decrypt(c_diff)
        expected = (m1 - m2) % pub.n

        assert decrypted == expected


class TestRSAHomomorphism:
    @pytest.fixture(scope="class")
    def rsa_keys(self):
        pub, priv = generate_rsa_keypair(bits=48)
        return pub, priv

    def test_rsa_roundtrip(self, rsa_keys):
        pub, priv = rsa_keys
        for m in [2, 5, 13, 42]:
            c = pub.encrypt(m)
            assert priv.decrypt(c) == m

    @pytest.mark.parametrize("m1, m2", [(3, 5), (7, 11), (2, 23)])
    def test_rsa_multiplication(self, rsa_keys, m1, m2):
        pub, priv = rsa_keys
        c1 = pub.encrypt(m1)
        c2 = pub.encrypt(m2)

        c_prod = rsa_multiply(pub, c1, c2)
        decrypted = priv.decrypt(c_prod)
        expected = (m1 * m2) % pub.n

        assert decrypted == expected


class TestHardwareDecomposition:
    def test_trace_decomposition(self):
        decomp = trace_hardware_decomposition(operand_a=15, operand_b=11, word_size_bits=4)
        assert decomp["word_size_bits"] == 4
        assert decomp["operand_a_word"] == 15
        assert decomp["operand_b_word"] == 11
        assert decomp["integer_sum"] == 26
        assert decomp["mod_4_residue"] == 2
        assert decomp["mod_4_overflow"] == 6

        # Check required hardware modules are identified
        modules = decomp["qca_modules_required"]
        assert "Multiplier_2x2.qca" in modules["partial_product_generation"]
        assert "RCA_4bit.qca" in modules["carry_ripple_accumulation"]
        assert "Modular_Adder.qca" in modules["modular_residue_reduction"]
