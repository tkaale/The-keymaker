ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shift_characters(word, shift):
    word_list = []
    for letter in word:
        letter_number = ALPHABET.index(letter)
        new_letter_number = letter_number + shift
        if new_letter_number > 25 and new_letter_number <= 50:
            new_letter_number -= 26
            word_list.append(ALPHABET[new_letter_number])
            continue
        if new_letter_number >= 51:
            new_letter_number -= 52
            word_list.append(ALPHABET[new_letter_number])
            continue
        else:
            word_list.append(ALPHABET[new_letter_number])
    return ''.join(word_list)


def pad_up_to(word, shift, n):
    word_list = []
    word = word
    word_list.append(word)
    while True:
        if len(''.join(word_list)) <= n:
            word = shift_characters(word, shift)
            word_list.append(word)
            continue
        else:
            break
    word_list = ''.join(word_list)
    return word_list[0: n]

#print(pad_up_to('aaa', 40, 10))


def abc_mirror(word):
    word_list = []
    for letter in word:
        last_index = len(ALPHABET) - 1
        letter_index = ALPHABET.index(letter)
        changed_letter = last_index - letter_index
        word_list.append(ALPHABET[changed_letter])
    return word_list

# print(abc_mirror('abcdefghijklm'))


def create_matrix(word_1, word_2):  # az, #abz
    word_list = []
    for letter in word_2:
        word = []
        shift = ALPHABET.index(letter)
        for letter in word_1:
            changed = shift_characters(letter, shift)
            word.append(changed)
        word_list.append(''.join(word))
    return word_list

#print( create_matrix('mamas', 'papas'))


def zig_zag_concatenate(list_of_words):
    coded_list = []
    odd_even = []
    number = 0
    for letter in list_of_words[0]:
        odd_even.append(number)
        number += 1
    for number in odd_even:
        if number % 2 == 0:
            for i in range(len(list_of_words)):
                coded_list.append(list_of_words[i][number])
        else:
            for i in reversed(range(len(list_of_words))):
                coded_list.append(list_of_words[i][number])
    return coded_list


#print(zig_zag_concatenate(['aaaa', 'bbbb', 'cccc', 'dddd']))

def rotate_right(word, n):
    word = word[-n:] + word[:-n]
    return word

#print(rotate_right('hello', 2))

