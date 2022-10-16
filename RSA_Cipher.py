import math
import random

def gcd(a , b):
    return gcd(a, b)

def modInverse(a, b):
    for i in range(1, b):
        if(a * i) % b == 1:
            return i
    return -1

def isPrime(a):
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(a)) + 1, 2):
            if a % i == 0:
                return False
    return True

def generateKey(key_size):
    a = random.randint(1,100)
    b = random.randint(1,100)

    # Ensure that do not choose the same prime number
    while a == b:
        a = random.randint(1,100)
    
    c = a * b
    phi = (a - 1) * (b - 1)

    # Public Key
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        # Private key
        d = modInverse(e, phi)
        if g == 1 and e != d:
            break

    return((e, c) , (d, c))

def encrypt(message, public_key):
    e, c = public_key

    return [pow(ord(i), e, c) for i in message]

def decrypt(message, private_key):
    d, c = private_key

    return ''.join([chr(pow(i, d, c)) for i in message])
