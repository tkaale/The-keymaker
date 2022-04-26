

def shift_characters(word, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word_list = []
    for letter in word:
        letter_number = alphabet.index(letter)
        new_letter_number = letter_number + shift
        print(new_letter_number)
        if new_letter_number > len(alphabet) - 1 and new_letter_number <= 50:
            new_letter_number -= 26
            word_list.append(alphabet[new_letter_number])
        if new_letter_number >= 51:
            new_letter_number -= 52
            word_list.append(alphabet[new_letter_number])
        else:
            word_list.append(alphabet[new_letter_number])
    if len(word_list) > len(word):
        word_list.pop()
    return word_list


print(shift_characters('ola', 50))