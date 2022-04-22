

def shift_characters(word, shift):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    word_list = []
    for letter in word:
        letter_number = alphabet[letter]
        if shift > 0:
            new_letter_number = letter_number + shift
            if letter_number > 26:
                    
            for key, value in alphabet.items():
                if new_letter_number == value:
                    letter = key
            word_list.append(letter)


shift_characters('ola', 1)