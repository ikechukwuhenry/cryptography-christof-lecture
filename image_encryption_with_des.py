from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import io

def encrypt_image(image_path, key):
    # Open the image file
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Encrypt the image data
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_image_data = cipher.encrypt(pad(image_data, DES.block_size))

    return encrypted_image_data

def decrypt_image(encrypted_image_data, key):
    # Decrypt the image data
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_image_data = unpad(cipher.decrypt(encrypted_image_data), DES.block_size)

    return decrypted_image_data

def save_image(data, output_path):
    # Create an image from the decrypted data and save it
    image = Image.open(io.BytesIO(data))
    image.save(output_path)

# Example usage:
secret_key = get_random_bytes(8)  # 64-bit key for DES
input_image_path = 'digital_camera_photo.jpg'
encrypted_output_path = 'encrypted_image.jpg'
decrypted_output_path = 'decrypted_image.jpg'

# Encrypt the image
encrypted_data = encrypt_image(input_image_path, secret_key)

# Save the encrypted image
with open(encrypted_output_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Decrypt the image
decrypted_data = decrypt_image(encrypted_data, secret_key)

# Save the decrypted image
save_image(decrypted_data, decrypted_output_path)