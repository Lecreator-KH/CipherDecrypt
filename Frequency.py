from operator import itemgetter
import string

# From http://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
# List sorted from A - Z, So The first item is in the list is A
englishFrequency = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
english_length = 26
ordA = ord('A')

def letterFreq(message):
    letter_counter = [0] * english_length

    for i in message:
        letter_counter[ord(i) - ordA] += 1
    
    total = sum(letter_counter)

    for i in range(len(letter_counter)):
        letter_counter[i] /= (float (total/100))
    
    return letter_counter

def compare(letter_counter, shift):
    score = 0

    for i in range(english_length):
        shift_index = (i + shift) % english_length
        score += abs(letter_counter[i] - (englishFrequency[shift_index]))

    return score