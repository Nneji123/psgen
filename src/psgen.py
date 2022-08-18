#!/usr/bin/env python3

# Author: Ifeanyi Nneji (Nneji123)
# Github: https://github.com/Nneji123
# Compatible with python 3


from __future__ import annotations

import random
import array
import argparse

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LOCASE_CHARACTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

UPCASE_CHARACTERS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

SYMBOLS = [
    "@",
    "#",
    "$",
    "%",
    "=",
    ":",
    "?",
    ".",
    "/",
    "|",
    "~",
    ">",
    "*",
    "(",
    ")",
    "<",
]


def generate_password_all(MAX_LEN: int) -> str:

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_no_digit(MAX_LEN: int) -> str:
    """
    The generate_password_no_digit function generates a password that does not contain any digits.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Determine the length of the password

    Returns:
        A string of characters that is the length of max_len

    Doc Author:
        Ifeanyi Nneji
    """

    COMBINED_LIST = UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_no_upcase(MAX_LEN: int) -> str:

    COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_no_locase(MAX_LEN: int) -> str:

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_no_symbol(MAX_LEN: int) -> str:

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)

    temp_pass = rand_digit + rand_upper + rand_lower

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_only_digits(MAX_LEN: int) -> str:

    COMBINED_LIST = DIGITS

    rand_digit = random.choice(DIGITS)

    temp_pass = rand_digit

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_only_upcase(MAX_LEN: int) -> str:

    COMBINED_LIST = UPCASE_CHARACTERS

    rand_upper = random.choice(UPCASE_CHARACTERS)

    temp_pass = rand_upper

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_only_locase(MAX_LEN: int) -> str:

    COMBINED_LIST = LOCASE_CHARACTERS

    rand_lower = random.choice(LOCASE_CHARACTERS)

    temp_pass = rand_lower

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


def generate_password_only_symbols(MAX_LEN: int) -> str:

    COMBINED_LIST = SYMBOLS

    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x
    return str(password)


# print out password
myparser = argparse.ArgumentParser(
    prog="psgen",
    description="Generate a random password with numbers, symbols and letters.",
    epilog="Happy password creating! :)",
)
myparser.add_argument(
    "--number",
    action="store",
    type=int,
    default=12,
    help="Write the length of the password you want to generate.The default value is 12. Example psgen --number 12",
)


myparser.add_argument(
    "--nodigit",
    action="store",
    type=int,
    default=12,
    help="Write the length of the password you want to generate.The default value is 12. Example psgen --nodigit true",
)

myparser.add_argument(
    "--noupcase",
    action="store",
    type=int,
    default=12,
    help="Write the length of the password you want to generate.The default value is 12. Example psgen --nodigit true",
)


def main():
    args = myparser.parse_args()
    input_number = args.number
    print(generate_password_all(input_number))


def arguments(args=myparser.parse_args()):
    nodigit = args.nodigit
    noupcase = args.noupcase
    if nodigit:
        print(generate_password_no_digit(nodigit))
    if noupcase:
        print(generate_password_no_upcase(noupcase))
    # args.func()

# Run the appropriate function (in this case showtop20 or listapps)


if __name__ == "__main__":
    main()
