import base64
import hashlib

def encode_base64(text):
    """Encode text using Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_text):
    """Decode Base64 encoded text."""
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes.decode('utf-8')

def encode_sha1(text):
    """Encode text using SHA-1 hash."""
    sha1_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    return sha1_hash

def encode_md5(text):
    """Encode text using MD5 hash."""
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

# Main functionality
if __name__ == "__main__":
    print("Hello welcom to script algoritm aqa bullet:")
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. SHA1 Encode")
    print("4. MD5 Encode")
    
    choice = input("Enter the number corresponding to your choice: ")

    text = input("Enter the text: ")

    if choice == '1':
        print(f"Base64 Encoded: {encode_base64(text)}")
    elif choice == '2':
        print(f"Base64 Decoded: {decode_base64(text)}")
    elif choice == '3':
        print(f"SHA1 Encoded: {encode_sha1(text)}")
    elif choice == '4':
        print(f"MD5 Encoded: {encode_md5(text)}")
    else:
        print("Invalid option")
