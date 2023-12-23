from rsa_example import keys_generator, encryption, decryption

public_key, private_key = keys_generator(8)
def sign_message(message, public_key):
    # n, e = public_key
    return encryption(message, public_key)
def verify(message, signed_msg, private_key):
    valid = False
    return message == decryption(signed_msg, private_key)


# Example usage
unsigned_message = "bsc cert"
signed_msg = sign_message(unsigned_message, public_key)
print(verify(unsigned_message, signed_msg, private_key))