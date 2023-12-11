from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode(), DES3.block_size))
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    return decrypted_message.decode()


# Example usage:
secret_key = get_random_bytes(24)  # 192-bit key for 3DES
original_message = "Hello, 3DES!"

encrypted_message = encrypt(original_message, secret_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, secret_key)
print("Decrypted Message:", decrypted_message)