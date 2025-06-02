from cryptography.fernet import Fernet

# Load the key from the key file
def load_key():
    return open("key.key", "rb").read()

# Decrypt the encrypted file
def decrypt_file(encrypted_file_path, output_file_path):
    key = load_key()
    fernet = Fernet(key)

    try:
        # Read encrypted data
        with open(encrypted_file_path, "rb") as file:
            encrypted_data = file.read()

        # Decrypt it
        decrypted_data = fernet.decrypt(encrypted_data)

        # Save decrypted data
        with open(output_file_path, "wb") as file:
            file.write(decrypted_data)

        print(f"\nDecryption successful. Decrypted file saved as '{output_file_path}'.")

    except Exception as e:
        print("\nDecryption failed:", str(e))


# === Main Program ===

try:
    encrypted_file = input("Enter the path of the file you want to decrypt: ").strip()

    if encrypted_file.endswith(".encrypted"):
        decrypted_file = encrypted_file[:-10]
    else:
        decrypted_file = encrypted_file + ".decrypted"

    decrypt_file(encrypted_file, decrypted_file)

except Exception as ex:
    print("\nUnexpected error:", str(ex))

input("\nPress Enter to exit...")

