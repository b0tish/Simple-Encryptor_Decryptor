import random

def generate_key(tempkey):
    key = 1
    for loop2 in tempkey:
        key = ord(loop2) + key
    for digit in str(key):
        key += int(digit)
    return key

def encrypt_message(message, tempkey):
    key = generate_key(tempkey)
    char_num = 40
    LETTERS_chooser = open("letter.txt", "r").readlines()
    LETTERS_rng = random.randint(0, 9)
    LETTERS = LETTERS_chooser[LETTERS_rng]

    char_letter = chr(char_num + LETTERS_rng)
    random_encry = random.randint(1, 3)
    letter_for_encry = 33 + random_encry

    encrypted = ""
    for chars in str(message):
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num + key) % 95
            encrypted += LETTERS[num:num+random_encry]
    encrypted += chr(letter_for_encry) + char_letter
    return encrypted

def decrypt_message(message, tempkey):
    key = generate_key(tempkey)

    n=0
    m=1
    user_list = []
    words = []
    random_var = 0
    main_var = 0

    try:
       char = message[-1]
    except:
        char = "0"


    LETTERS_choosing = ord(char) - 40
    message = message[:-1]

    #for random_var
    char_random_encry = message[-1]
    random_var = ord(char_random_encry) - 33
    message = message.strip(message[len(message) - 1])

    LETTERS_chooser = open("letter.txt", "r").readlines()
    LETTERS = LETTERS_chooser[int(LETTERS_choosing)]

    decrypted = ""
    i = random_var - 1
    main_var = random_var - 1
    for chars in str(message):
        if main_var == i:
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num = (num - key) % 95
                decrypted += LETTERS[num]
                i = 0
        else:
            i += 1
    return decrypted
