import string
from collections import Counter

def get_frequency(text):
    letters = [c for c in text if c.isalpha()]
    letter_count = Counter(letters)
    return {char: count / len(letters) for char, count in letter_count.items()}

def decipher(text, key):
    deciphered_text = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            new_char = key.get(char.lower(), char.lower())
            if is_upper:
                new_char = new_char.upper()
            deciphered_text.append(new_char)
        else:
            deciphered_text.append(char)
    return ''.join(deciphered_text)

def solve_cryptogram(ciphertext):
    english_frequencies = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978,
        'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074
    }

    ciphertext_frequencies = get_frequency(ciphertext)
    sorted_english_frequencies = sorted(english_frequencies.keys(), key=lambda x: english_frequencies[x], reverse=True)
    sorted_ciphertext_frequencies = sorted(ciphertext_frequencies.keys(), key=lambda x: ciphertext_frequencies[x], reverse=True)

    key = dict(zip(sorted_ciphertext_frequencies, sorted_english_frequencies))
    plaintext = decipher(ciphertext, key)
    return plaintext

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    plaintext = solve_cryptogram(ciphertext)
    print("Decrypted text:", plaintext)
