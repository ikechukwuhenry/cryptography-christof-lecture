# pip install cryptography
# This is a basic example using AES in Cipher Feedback (CFB) mode.

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def encrypt(message, key):
    iv = urandom(16)  # Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode()


# Example usage:
secret_key = urandom(32)  # 256-bit key
original_message = "Hello, AES!"

encrypted_message = encrypt(original_message, secret_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, secret_key)
print("Decrypted Message:", decrypted_message)