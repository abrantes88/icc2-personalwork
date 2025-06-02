from cryptography.fernet import Fernet

# Replace with your actual key (must be base64-encoded, 32 bytes when decoded)
key = b'insert the key you want to use'


# Encrypted token (must also be a byte string)
encrypted_data = b'insert the message you want to decode'

# Initialize Fernet with your key
fernet = Fernet(key)

try:
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)
    print("Decrypted data:", decrypted_data.decode())
except Exception as e:
    print("Decryption failed:", str(e))

input("\nPress Enter to exit...") 