import string

# From http://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
# List sorted from A - Z, So The first item is in the list is A
englishFrequency = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
english = "abcdefghijklmnopqrstuvwxyz"

def letterCounter(message):
    letter_counter = dict.fromkeys(string.ascii_lowercase, 0)
    letter_count = 0

    for i in message:
       if i in english:
            letter_counter[i] += 1
            letter_count += 1

    return letter_counter