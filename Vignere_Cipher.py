import string
import Frequency

frequency = Frequency
english = "abcdefghijklmnopqrstuvwxyz"

def subString(string, seperation):
    return [string[i::seperation] for i in range(seperation)]

def generateKey(key):
    # Store the index of the character
    index = []
    for i in key:
        index.append(english.find(i))
    return index

def encrypt(message, key):
    encrypted_message = ""
    key = generateKey(key)
    counter = 0
    for i in message:
        if counter == len(key):
            counter = 0
        if i == ' ':
            encrypted_message += i
        else:
            mPos = (english.find(i) + key[counter]) % 26
            encrypted_message += english[mPos]
        counter += 1
    
    return ''.join(encrypted_message)

def decrypt(message, key):
    decrypted_message = ""
    key = generateKey(key)
    counter = 0
    for i in message:
        if counter == len(key):
            counter = 0
        if i == ' ':
            decrypted_message += i
        else:
            mPos = (english.find(i) - key[counter]) % 26
            decrypted_message += english[mPos]
        counter += 1
    
    return ''.join(decrypted_message)