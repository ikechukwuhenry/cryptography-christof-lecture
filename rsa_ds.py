# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import serialization


# import os

# # Generate a byte array of length 16 (for example)
# key_bytes = os.urandom(16)

# print(key_bytes)


# # Generate an RSA private key
# private_key = serialization.load_pem_private_key(
#     key_bytes,
#     password=None,
#     backend=default_backend()
# )
# public_key = private_key.public_key()

# # Create a message
# message = b"Hello, RSA!"

# # Sign the message using the private key
# signature = private_key.sign(
#     message,
#     padding.PKCS1v15(),
#     hashes.SHA256()
# )

# print(f"Signature: {signature.hex()}")

# # Verify the signature using the public key
# try:
#     public_key.verify(
#         signature,
#         message,
#         padding.PKCS1v15(),
#         hashes.SHA256()
#     )
#     print("Signature is valid.")
# except:
#     print("Signature is invalid.")
