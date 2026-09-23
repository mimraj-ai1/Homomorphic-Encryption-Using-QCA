"""
Homomorphic Ciphertext Operations and QCA Hardware Architectural Mapping.

Implements:
1. Paillier Homomorphic Addition:
   c_sum = (c1 * c2) mod n^2
2. Paillier Homomorphic Scalar Multiplication:
   c_prod = (c1 ^ k) mod n^2
3. Paillier Homomorphic Subtraction:
   c_diff = (c1 * c2^-1) mod n^2
4. RSA Homomorphic Multiplication:
   c_prod = (c1 * c2) mod N
5. Hardware Mapping & Decomposition:
   Shows how large-word modular arithmetic breaks down into QCA logic gates,
   multipliers, ripple carry adders, and modular reduction units.
"""

from typing import Dict, List, Tuple
from encryption import PaillierPublicKey, RSAPublicKey, mod_inverse


def paillier_add(pubkey: PaillierPublicKey, c1: int, c2: int) -> int:
    """
    Homomorphically adds two encrypted ciphertexts:
    c_add = c1 * c2 (mod n^2)
    Decryption of c_add yields (m1 + m2) mod n.
    """
    return (c1 * c2) % pubkey.n_sq


def paillier_add_plain(pubkey: PaillierPublicKey, c: int, m_plain: int) -> int:
    """
    Homomorphically adds a plaintext constant to an encrypted ciphertext:
    c_add = c * g^m_plain (mod n^2)
    Decryption yields (m + m_plain) mod n.
    """
    return (c * pow(pubkey.g, m_plain, pubkey.n_sq)) % pubkey.n_sq


def paillier_multiply_scalar(pubkey: PaillierPublicKey, c: int, k: int) -> int:
    """
    Homomorphically multiplies an encrypted ciphertext by a plaintext scalar k:
    c_mult = c^k (mod n^2)
    Decryption yields (k * m) mod n.
    """
    return pow(c, k, pubkey.n_sq)


def paillier_subtract(pubkey: PaillierPublicKey, c1: int, c2: int) -> int:
    """
    Homomorphically subtracts c2 from c1:
    c_diff = c1 * (c2^-1) (mod n^2)
    Decryption yields (m1 - m2) mod n.
    """
    c2_inv = mod_inverse(c2, pubkey.n_sq)
    return (c1 * c2_inv) % pubkey.n_sq


def rsa_multiply(pubkey: RSAPublicKey, c1: int, c2: int) -> int:
    """
    Homomorphically multiplies two RSA ciphertexts:
    c_prod = c1 * c2 (mod N)
    Decryption yields (m1 * m2) mod N.
    """
    return (c1 * c2) % pubkey.n


def trace_hardware_decomposition(operand_a: int, operand_b: int, word_size_bits: int = 4) -> Dict:
    """
    Analyzes how a binary modular arithmetic operation maps to QCA physical hardware modules:
    - 2x2 Multiplier slices for partial products
    - Full Adders and 4-bit Ripple Carry Adders for operand accumulation
    - Modular Adders for residue reduction
    """
    mask = (1 << word_size_bits) - 1
    a_word = operand_a & mask
    b_word = operand_b & mask

    # 1. Partial products breakdown (using 2-bit slices)
    slices_a = [a_word & 0b11, (a_word >> 2) & 0b11]
    slices_b = [b_word & 0b11, (b_word >> 2) & 0b11]

    partial_products_2x2 = []
    for i, sa in enumerate(slices_a):
        for j, sb in enumerate(slices_b):
            partial_products_2x2.append({
                "slice_a": sa,
                "slice_b": sb,
                "product": sa * sb,
                "bit_weight": (i + j) * 2,
            })

    # 2. Integer sum and modular reduction
    sum_full = a_word + b_word
    mod_4_residue = sum_full % 4
    mod_4_overflow = sum_full // 4

    return {
        "word_size_bits": word_size_bits,
        "operand_a_word": a_word,
        "operand_b_word": b_word,
        "partial_products_2x2": partial_products_2x2,
        "integer_sum": sum_full,
        "mod_4_residue": mod_4_residue,
        "mod_4_overflow": mod_4_overflow,
        "qca_modules_required": {
            "partial_product_generation": "QCA 2x2 Multipliers (Multiplier_2x2.qca)",
            "carry_ripple_accumulation": "QCA 4-bit RCA (RCA_4bit.qca) / Full Adders (Full_Adder.qca)",
            "modular_residue_reduction": "QCA 2-bit Modular Adder (Modular_Adder.qca)",
            "primitive_logic": "QCA AND/OR/NOT/XOR Gates",
        },
    }
