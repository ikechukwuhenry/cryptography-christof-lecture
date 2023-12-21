def key_generator():
    pass

def encryption(plaintext, encryption_key, n):
    return (plaintext**encryption_key) % n

def decryption(ciphertext, decryption_key, n):
    return (ciphertext**decryption_key) % n

print(encryption(4, 3, 33))
print(decryption(31, 7, 33))

