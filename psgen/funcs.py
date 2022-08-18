#!/usr/bin/env python3

# Author: Ifeanyi Nneji (Nneji123)
# Github: https://github.com/Nneji123
# Compatible with python 3


from __future__ import annotations

import random
import array

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
    """
    The generate_password_all function generates a password of the length specified by MAX_LEN.
    The password is generated using the following characters: digits, uppercase letters, lowercase letters and symbols.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Determine the length of the password

    Returns:
        A string of randomly generated characters

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_no_upcase function generates a password of the desired length,
    without any uppercase characters. The function takes one argument, MAX_LEN (an integer),
    and returns a string.

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_no_locase function generates a password that is comprised of digits, uppercase characters, and symbols. The function takes one argument: MAX_LEN (an integer). It then generates a random digit from the DIGITS list using the random.choice() function. It also chooses a random character from the UPCASE_CHARACTERS list using another call to random.choice(). Lastly it chooses a symbol from SYMBOLS and appends all three of these randomly generated characters to form an initial temporary password string called temp_pass.

    The for loop iterates over range(MAX_LEN - 4) which means that it

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password that is

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_no_symbol function generates a password with no symbols.
    It takes one parameter, MAX_LEN, which is the maximum length of the password.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Define the maximum length of the password

    Returns:
        A password with no symbols

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_only_digits function generates a password that is only comprised of digits.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is a combination of digits with no special characters

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_only_upcase function generates a password that is only comprised of uppercase characters.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is only comprised of uppercase characters

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_only_locase function generates a password that is comprised of only lowercase characters.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password that is all lowercase letters

    Doc Author:
        Ifeanyi Nneji
    """

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
    """
    The generate_password_only_symbols function generates a password that is comprised of only symbols.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is

    Doc Author:
        Ifeanyi Nneji
    """

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
