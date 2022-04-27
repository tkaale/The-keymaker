

from re import A


def shift_characters(word, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    word_list = []
    for letter in word:
        letter_number = alphabet.index(letter)
        new_letter_number = letter_number + shift
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
    return ''.join(word_list)



def pad_up_to(word, shift, n):
    word_list = []
    word = word
    while True:
        if len(''.join(word_list)) <= n:
            word = shift_characters(word, shift)
            word_list.append(word)
            continue
        else:
            break
    word_list = ''.join(word_list)
    return word_list[0: n]

print(pad_up_to('aaa', 2, 10))

