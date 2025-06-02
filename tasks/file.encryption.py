from cryptography.fernet import Fernet

# === Functions ===

def write_key():
    """Generate a new key and save it into a file"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the key from the current directory named `key.key`"""
    return open("key.key", "rb").read()

def encrypt_file(file_path, output_path):
    """Encrypt the contents of a file and save the result"""
    key = load_key()
    fernet = Fernet(key)

    # Read the original file in binary mode
    with open(file_path, "rb") as file:
        original = file.read()

    # Encrypt the file contents
    encrypted = fernet.encrypt(original)

    # Write the encrypted contents to a new file
    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"File '{file_path}' encrypted and saved as '{output_path}'.")


# === Main ===

# Generate a key once (optional if you already have a key)
write_key()

input_file = input("Enter the path to the file you want to encrypt: ").strip()
output_file = input_file + ".encrypted"

# Encrypt the file
encrypt_file(input_file, output_file)

input("\nPress Enter to exit...") 
