import random

# Function to calculate modular exponentiation (base^exp mod mod)
def power_mod(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman Key Exchange
def diffie_hellman(p, g):
    # User A selects a secret private key (a) and computes public key A = g^a mod p
    a = random.randint(1, p - 1)
    A = power_mod(g, a, p)
    print(f"User A's private key: {a}")
    print(f"User A's public key (A): {A}")

    # User B selects a secret private key (b) and computes public key B = g^b mod p
    b = random.randint(1, p - 1)
    B = power_mod(g, b, p)
    print(f"User B's private key: {b}")
    print(f"User B's public key (B): {B}")

    # User A and User B exchange public keys (A and B) and calculate the shared secret
    # User A computes the shared secret S = B^a mod p
    S_A = power_mod(B, a, p)
    print(f"User A's shared secret (S_A): {S_A}")

    # User B computes the shared secret S = A^b mod p
    S_B = power_mod(A, b, p)
    print(f"User B's shared secret (S_B): {S_B}")

    # Both shared secrets should match
    if S_A == S_B:
        print("Shared secret exchange successful!")
        print(f"The shared secret is: {S_A}")
    else:
        print("Shared secret exchange failed.")

# Example values for p and g (prime number and primitive root modulo p)
p = 23  # A small prime number
g = 5   # A primitive root modulo p

# Run Diffie-Hellman Key Exchange
diffie_hellman(p, g)
