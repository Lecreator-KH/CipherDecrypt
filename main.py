import string
import Vignere_Cipher
import sys
import os

def switch(cipher, text, key, choice):
    if cipher == 'Vignere':
        cipher = Vignere_Cipher
        if choice == 'E':
            text = cipher.encrypt(text, key)
        elif choice == 'D':
            if(key != ""):
                text = cipher.decrypt(text, key)
            else:
                return "To be implented"
        return text

# Function to remove all spaces contains in the text
def removeSpace(text):
    return "".join(text.split())

# Function to convert all text to lowercase
def lowerCase(text):
    return text.lower()

def upperCase(text):
    return text.upper()

def main():
    print("Cipher List: Vignere")
    cipher = input("Which cipher you want to use: ")

    choice = input("Do you want to Encrypt 'E' or Decrypt 'D': ")

    input_text = input("Enter message: ")

    key = input("Enter key: ")

    output_text = upperCase(switch(cipher, lowerCase(input_text), lowerCase(key), choice))
    print(output_text)

if __name__ == '__main__':
    main()

