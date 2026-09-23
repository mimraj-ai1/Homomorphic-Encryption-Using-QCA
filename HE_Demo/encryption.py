"""
Homomorphic Encryption Engine: Key Generation, Encryption, and Decryption.

Implements:
1. Paillier Cryptosystem (Additive Homomorphic Encryption):
   - Decrypt(E(m1) * E(m2) mod n^2) = (m1 + m2) mod n
   - Decrypt(E(m1)^k mod n^2) = (k * m1) mod n
2. Multiplicative Homomorphic Scheme (Unpadded RSA Homomorphism):
   - Decrypt(E(m1) * E(m2) mod N) = (m1 * m2) mod N
3. Low-level cryptographic primitives:
   - Miller-Rabin probabilistic primality test
   - Extended Euclidean Algorithm for modular inverse
   - Greatest Common Divisor and Least Common Multiple
"""

import math
import secrets
from typing import Tuple


def gcd(a: int, b: int) -> int:
    """Computes greatest common divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """Computes least common multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def mod_inverse(a: int, m: int) -> int:
    """Computes modular multiplicative inverse: a * x = 1 (mod m)."""
    if math.gcd(a, m) != 1:
        raise ValueError(f"Modular inverse does not exist for a={a}, m={m}")
    return pow(a, -1, m)


def is_prime(n: int, k: int = 40) -> bool:
    """
    Miller-Rabin probabilistic primality test.
    k represents the number of testing rounds (error probability <= 4^(-k)).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Write n - 1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def generate_prime(bits: int) -> int:
    """Generates a cryptographically strong random prime of specified bit-length."""
    while True:
        # Ensure highest and lowest bits are set
        candidate = (secrets.randbits(bits) | (1 << (bits - 1)) | 1)
        if is_prime(candidate):
            return candidate


# =============================================================================
# PAILLIER CRYPTOSYSTEM (Additive Homomorphism)
# =============================================================================

class PaillierPublicKey:
    """Represents a Paillier public encryption key (n, g)."""

    def __init__(self, n: int, g: int):
        self.n = n
        self.n_sq = n * n
        self.g = g

    def encrypt(self, m: int, r: int = None) -> int:
        """
        Encrypts plaintext message m in Z_n:
        c = g^m * r^n (mod n^2)
        """
        if not (0 <= m < self.n):
            raise ValueError(f"Message m must satisfy 0 <= m < n (n={self.n})")

        if r is None:
            # Pick random blinding factor r in Z_n*
            while True:
                r = secrets.randbelow(self.n - 1) + 1
                if gcd(r, self.n) == 1:
                    break

        c = (pow(self.g, m, self.n_sq) * pow(r, self.n, self.n_sq)) % self.n_sq
        return c


class PaillierPrivateKey:
    """Represents a Paillier private decryption key (lambda, mu, n)."""

    def __init__(self, lam: int, mu: int, n: int):
        self.lam = lam
        self.mu = mu
        self.n = n
        self.n_sq = n * n

    def decrypt(self, c: int) -> int:
        """
        Decrypts ciphertext c in Z_n^2*:
        m = L(c^lambda mod n^2) * mu (mod n)
        where L(u) = (u - 1) // n
        """
        u = pow(c, self.lam, self.n_sq)
        l_u = (u - 1) // self.n
        m = (l_u * self.mu) % self.n
        return m


def generate_paillier_keypair(bits: int = 64) -> Tuple[PaillierPublicKey, PaillierPrivateKey]:
    """
    Generates a Paillier keypair:
    1. Select two independent primes p, q of length bits // 2
    2. n = p * q
    3. lambda = lcm(p-1, q-1)
    4. g = n + 1 (standard simplified base)
    5. mu = (L(g^lambda mod n^2))^-1 mod n
    """
    prime_bits = max(16, bits // 2)
    while True:
        p = generate_prime(prime_bits)
        q = generate_prime(prime_bits)
        if p != q:
            n = p * q
            lam = lcm(p - 1, q - 1)
            # Using standard g = n + 1:
            # L((n+1)^lambda mod n^2) = (1 + lambda*n - 1)//n = lambda
            # mu = lambda^-1 mod n
            try:
                mu = mod_inverse(lam, n)
                g = n + 1
                return PaillierPublicKey(n, g), PaillierPrivateKey(lam, mu, n)
            except ValueError:
                continue


# =============================================================================
# MULTIPLICATIVE HOMOMORPHIC SCHEME (Unpadded RSA Homomorphism)
# =============================================================================

class RSAPublicKey:
    """Represents an RSA public key (e, N) exhibiting multiplicative homomorphism."""

    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n

    def encrypt(self, m: int) -> int:
        """c = m^e (mod N)"""
        if not (0 <= m < self.n):
            raise ValueError(f"Message m must satisfy 0 <= m < N (N={self.n})")
        return pow(m, self.e, self.n)


class RSAPrivateKey:
    """Represents an RSA private key (d, N)."""

    def __init__(self, d: int, n: int):
        self.d = d
        self.n = n

    def decrypt(self, c: int) -> int:
        """m = c^d (mod N)"""
        return pow(c, self.d, self.n)


def generate_rsa_keypair(bits: int = 64) -> Tuple[RSAPublicKey, RSAPrivateKey]:
    """Generates an RSA keypair exhibiting multiplicative homomorphism."""
    prime_bits = max(16, bits // 2)
    e = 65537
    while True:
        p = generate_prime(prime_bits)
        q = generate_prime(prime_bits)
        if p != q:
            n = p * q
            phi = (p - 1) * (q - 1)
            if gcd(e, phi) == 1:
                try:
                    d = mod_inverse(e, phi)
                    return RSAPublicKey(e, n), RSAPrivateKey(d, n)
                except ValueError:
                    continue
