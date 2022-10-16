import string
import Frequency

english = "abcdefghijklmnopqrstuvwxyz"

def generateKey(self, key):
    # Store the index of the character
    index = []
    for i in key:
        index.append(english.find(i))
    return index

def encrypt(self, message, key):
    encrypted_message = ""
    key = self.generateKey(key)
    counter = 0
    for i in message:
        if counter == len(key):
            counter = 0
        if i == " ":
            encrypted_message += i
        else:
            mPos = (english.find(i) + key[counter]) % 26
            encrypted_message += english[mPos]
        counter += 1
    
    return ''.join(encrypted_message)

def decrypt(self, message, key):
    decrypted_message = ""
    key = self.generateKey(key)
    counter = 0
    for i in message:
        if counter == len(key):
            counter = 0
        if i == " ":
            decrypted_message += i
        else:
            mPos = (english.find(i) - key[counter]) % 26
            decrypted_message += english[mPos]
        counter += 1
    
    return ''.join(decrypted_message)
