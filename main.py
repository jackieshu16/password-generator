"""
Password requirements:
1. At least 10 characters (and up to 100 characters)
2. At least 3 of the following: uppercase, lowercase, numeric, or special characters.
   The allowed special characters are ~ ! @ # $ % ^ * - _ = + [ { ] } / ; : , . ?

After generating a password, verify the requirements met
"""
import logging
import random
import string

min_length = 10
allowed_special_char = "~!@#$%^*-_=+[{]}/;:,.?"


def uppercase_letters(length=1):
    upper_string = ''
    for i in range(length):
        upper_string += random.choice(string.ascii_letters).upper()
    return upper_string


def lowercase_letters(length=1):
    lower_string = ''
    for i in range(length):
        lower_string += random.choice(string.ascii_letters).lower()
    return lower_string


def numeric_value():
    return random.randint(0, 99999)


def special_characters(length=1):
    special_char_string = ''
    for i in range(length):
        special_char_string += random.choice(allowed_special_char)
    return special_char_string


def password_length(password):
    pass_len = len(password)
    print(f'password length is {pass_len}')
    return pass_len


def shuffle_string(initial_string):
    shuffled = ''.join(random.sample(initial_string, len(initial_string)))
    print(f'after shuffling, password is {shuffled}')
    return shuffled


def assemble_password():
    groups = ['upper', 'lower', 'numeric', 'special']
    # decide to use 3 or 4 groups
    num_of_groups_to_use = random.randint(3, 4)
    if num_of_groups_to_use == 3:
        # randomly pick 3 out of 4 groups
        pop_item = random.choice(groups)
        print(f'pop/not use group: {pop_item}')
        groups.remove(pop_item)
    password = ''
    for group in groups:
        if group == 'upper':
            password += uppercase_letters(random.randint(1, min_length))
        if group == 'lower':
            password += lowercase_letters(random.randint(1, min_length))
        if group == 'numeric':
            password += str(numeric_value())
        if group == 'special':
            password += special_characters(random.randint(1, min_length))
    print(f'assembled password is {password}')
    if password_length(password) < min_length:
        password += lowercase_letters(min_length - password_length(password))
        print(f'after filling, password is {password}')
    return password


shuffle_string(assemble_password())
