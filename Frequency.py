from operator import le
import string

# From http://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
# 
englishFrequency = {'E': 12.702, 'T': 9.056, 'A': 8.167, 'O': 7.507, 'I': 6.966, 'N': 6.749, 'S': 6.327, 'H': 6.094, 'R': 5.987, 'D': 4.253, 'L': 4.025, 'C': 2.782, 'U': 2.758, 'M': 2.406, 'W': 2.360, 'F': 2.228, 'G': 2.015, 'Y': 1.974, 'P': 1.929, 'B': 1.492, 'V': 0.978, 'K': 0.772, 'J': 0.153, 'X': 0.150, 'Q': 0.095, 'Z': 0.074}
english = "abcdefghijklmnopqrstuvwxyz"
etoin = "etaoinshrdlcumwfgypbvkjxqz"

# 
def letterCounter(message):
    letter_counter = dict.fromkeys(string.ascii_lowercase, 0)
    letter_count = 0

    for i in message:
       if i in english:
            letter_counter[i] += 1
            letter_count += 1

    return letter_counter

