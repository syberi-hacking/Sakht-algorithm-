import hashlib
import base64
import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def sha1_encode(text):
    """Encode text using SHA1."""
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    return sha1_hash

def base64_encode(text):
    """Encode text using Base64."""
    base64_encoded = base64.b64encode(text.encode()).decode()
    return base64_encoded

def md5_encode(text):
    """Encode text using MD5."""
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

def rsa_base64_encode(text):
    """Encrypt text using RSA and encode it in Base64."""
    (public_key, private_key) = rsa.newkeys(512)
    encrypted = rsa.encrypt(text.encode(), public_key)
    base64_encoded = base64.b64encode(encrypted).decode()
    return base64_encoded

def aes_256_encode(text, key):
    """Encrypt text using AES 256-bit encryption and encode it in Base64."""
    key = hashlib.sha256(key.encode()).digest()  # Ensure the key is 32 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)  # Using zero IV for simplicity
    encrypted = cipher.encrypt(pad(text.encode(), AES.block_size))
    base64_encoded = base64.b64encode(encrypted).decode()
    return base64_encoded

def binary_encode(text):
    """Encode text into binary."""
    binary_encoded = ' '.join(format(ord(char), '08b') for char in text)
    return binary_encoded

def main():
    """Main bot function to get user input and perform encoding."""
    print("Welcome to the create algoritm bug aqa bullet")
    print("Supported algorithms: sha1, base64, md5, rsa-base64, aes-256bit, binary")
    
    text = input("Enter the text you want to encode: ")
    algorithm = input("Choose an encoding algorithm (sha1/base64/md5/rsa-base64/aes-256bit/binary): ").lower()

    if algorithm == "sha1":
        result = sha1_encode(text)
    elif algorithm == "base64":
        result = base64_encode(text)
    elif algorithm == "md5":
        result = md5_encode(text)
    elif algorithm == "rsa-base64":
        result = rsa_base64_encode(text)
    elif algorithm == "aes-256bit":
        key = input("Enter a key for AES encryption (use a strong key): ")
        result = aes_256_encode(text, key)
    elif algorithm == "binary":
        result = binary_encode(text)
    else:
        print("Invalid algorithm selected!")
        return

    print(f"Encoded result using {algorithm}: {result}")

if __name__ == "__main__":
    main()
