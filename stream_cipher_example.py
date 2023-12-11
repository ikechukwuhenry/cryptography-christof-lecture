from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def encrypt(message, key):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(message.encode())
    return ciphertext

def decrypt(ciphertext, key):
    cipher = ARC4.new(key)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode()

# Example usage:
secret_key = get_random_bytes(16)  # 128-bit key for RC4
original_message = "Hello, RC4 Stream Cipher!"

encrypted_message = encrypt(original_message, secret_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, secret_key)
print("Decrypted Message:", decrypted_message)



# A stream cipher is a type of symmetric-key cipher where each plaintext digit
# is encrypted one at a time with the corresponding digit of a 
# pseudorandom stream of key digits. One common example of a stream cipher
# is the RC4 algorithm.

# In this example, the ARC4 cipher from pycryptodome is used. 
# The key size for RC4 can vary, but in this case, we use a 
# 128-bit key (get_random_bytes(16)). 
# Keep in mind that RC4 is considered insecure for certain applications
#  due to vulnerabilities, and it's recommended to use more 
# modern stream ciphers like ChaCha20 or AES in counter mode for better security.