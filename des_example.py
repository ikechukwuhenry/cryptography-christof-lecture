# Here's a simple example of DES encryption and decryption in Python
# using the pycryptodome library
# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode(), DES.block_size))
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_message.decode()

# Example usage:
secret_key = get_random_bytes(8)  # 64-bit key for DES
original_message = "Hello, DES!"

encrypted_message = encrypt(original_message, secret_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, secret_key)
print("Decrypted Message:", decrypted_message)


# This example uses Electronic Codebook (ECB) mode for simplicity. 
# Note that ECB is not secure for large amounts of data, 
# and other modes like Cipher Block Chaining (CBC) should be used in practice.