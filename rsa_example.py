import random
from math import gcd

def square_multiply(base, exponent):
    x = base
    e = bin(exponent)[2:]
    result = x
    i = 1
    while i < (len(e)):
        # print("iteration ", i)
        result = result ** 2
        if e[i] == '1':
            result = result * x
        i = i + 1
    return result

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

# def is_prime(n):
#     """Check if a number is prime."""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

def generate_prime(bits=16):
    prime = random.getrandbits(bits)
    while not is_prime(prime):
        prime = random.getrandbits(bits)
    return prime

def mod_inverse(e, phi):
    """Compute the modular inverse using extended Euclidean algorithm."""
    m0, x0, x1 = phi, 0, 1
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    return x1 % m0 if e == 1 else None

def mod_inverse_variant(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    # raise ValueError("Mod inverse does not exist")
    return None

def keys_generator(bits=16):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi_n = (p -1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)
    if d is None:
        return keys_generator()
    
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key
    

# def encryption(plaintext, public_key):
#     n, e = public_key
#     ciphertext =[(ord(char)** e) % n for char in plaintext]
#     return ciphertext

# def decryption(ciphertext, private_key):
#     n, d = private_key
#     plaintext = ''.join([chr((text ** d) % n) for text in ciphertext])
#     return plaintext
def encryption(plaintext, public_key):
    n, e = public_key
    ciphertext =[(square_multiply(ord(char), e)) % n for char in plaintext]
    return ciphertext

def decryption(ciphertext, private_key):
    n, d = private_key
    plaintext = ''.join([chr((square_multiply(text, d)) % n) for text in ciphertext])
    return plaintext

# Example usage:
public_key, private_key = keys_generator(16)
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello am trying to break the code world RSA!"
encrypted_msg = encryption(message, public_key)
print("Encrypted:", encrypted_msg)

decrypted_msg = decryption(encrypted_msg, private_key)
print("Decrypted:", decrypted_msg)

