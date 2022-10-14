import string

# From http://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
# Tuple sorted from A - Z, So The first item is in the tuple is A
englishFrequency = (0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074)

# Function to remove all spaces contains in the message
def removeSpace(cipherText):
    return cipherText.strip()

# Function to convert all text within the message to lowercase
def lowerCase(cipherText):
    return cipherText.lower()

# 
def messageCompareFrequenct(cipherText):
    
    return