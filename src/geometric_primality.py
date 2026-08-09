"""
Geometric Primality Functions
==============================
Core functions for the geometric primality test based on
the n = 2a ± b representation network.

Part of Paper 2: Differential Behaviour of Primes mod 4
Author: Berramdane Reddouane
Date: August 2026
"""

import math

def is_prime_or_one(x: int) -> bool:
    """
    Check if x is 1 or prime.
    
    Args:
        x: integer to check
    
    Returns:
        True if x == 1 or x is prime
    """
    if x == 1:
        return True
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def count_minus_any(n: int, primes: list) -> int:
    """
    Count representations n = 2a - b where a,b in {1} U P.
    
    Args:
        n: odd integer to represent
        primes: list of primes up to n
    
    Returns:
        Number of minus representations
    """
    cnt = 0
    for a in primes:
        if a >= n:
            break
        b = 2 * a - n
        if b >= 1 and is_prime_or_one(int(b)):
            cnt += 1
    return cnt


def count_plus_any(n: int, primes: list) -> int:
    """
    Count representations n = 2a + b where a,b in {1} U P.
    
    Args:
        n: odd integer to represent
        primes: list of primes up to n
    
    Returns:
        Number of plus representations
    """
    cnt = 0
    for a in primes:
        if 2 * a >= n:
            break
        b = n - 2 * a
        if b >= 1 and is_prime_or_one(int(b)):
            cnt += 1
    return cnt


def geometric_primality_test(n: int, primes: list) -> bool:
    """
    Geometric primality test without trial division.
    
    Uses the representation counts R+ and R- to determine
    if n is likely prime.
    
    Args:
        n: odd integer to test
        primes: list of primes up to n
    
    Returns:
        True if n passes the geometric primality test
    """
    if n < 3 or n % 2 == 0:
        return False
    
    r_minus = count_minus_any(n, primes)
    r_plus = count_plus_any(n, primes)
    
    scale = n / (math.log(n) ** 2)
    sum_norm = (r_minus + r_plus) / scale
    ratio = r_plus / r_minus if r_minus > 0 else float('inf')
    
    # Condition (i): sum_norm threshold
    if sum_norm >= 2.1:
        return False
    
    # Condition (ii): ratio depends on mod-4 class
    if n % 4 == 1:
        if not (1.18 <= ratio <= 1.35):
            return False
    else:
        if not (1.10 <= ratio <= 1.25):
            return False
    
    return True


def features(n: int):
    """
    Compute geometric features of n within its square layer.
    
    Args:
        n: integer
    
    Returns:
        tuple: (low_sq, high_sq, dist_low, dist_high, nearest, t)
    """
    k = int(math.isqrt(n))
    low_sq = k * k
    high_sq = (k + 1) * (k + 1)
    dist_low = n - low_sq
    dist_high = high_sq - n
    t = (n - low_sq) / (high_sq - low_sq)
    return low_sq, high_sq, dist_low, dist_high, min(dist_low, dist_high), t
