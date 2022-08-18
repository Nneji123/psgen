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
    help="This will generate a random password with no digits. Example psgen --nodigit 12",
)

myparser.add_argument(
    "--noupcase",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with no uppercase letters. Example psgen --noupcase 12",
)

myparser.add_argument(
    "--nolowercase",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with no lowercase letters. Example psgen --nolowercase 12",
)

myparser.add_argument(
    "--nosymbols",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with no symbols. Example psgen --nosymbols 12",
)

myparser.add_argument(
    "--onlydigits",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with only digits. Example psgen --onlydigits 12",
)

myparser.add_argument(
    "--onlylocase",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with only lowercase letters. Example psgen --onlylocase 12",
)

myparser.add_argument(
    "--onlyupcase",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with only uppercase letters. Example psgen --onlyupcase 12",
)

myparser.add_argument(
    "--onlysymbols",
    action="store",
    type=int,
    default=12,
    help="This will generate a random password with only symbols. Example psgen --onlysymbols 12",
)


def main():
    """
    The main function of this program is to generate a password of the desired length.
    The password will be generated using random characters from the set of lowercase letters, uppercase letters, digits and symbols.


    Args:

    Returns:
        The list of generated passwords

    Doc Author:
        Trelent
    """
    args = myparser.parse_args()
    input_number = args.number
    print(generate_password_all(input_number))


def arguments(args=myparser.parse_args()):
    """
    The arguments function parses the arguments passed to the program at runtime.
    It then calls a function that generates a password based on those arguments.


    Args:
        args=myparser.parse_args(): Pass arguments to the function

    Returns:
        The values of the arguments passed to it

    Doc Author:
        Trelent
    """
    nodigit = args.nodigit
    noupcase = args.noupcase
    nolowercase = args.nolowercase
    nosymbols = args.nosymbols
    onlydigits = args.onlydigits
    onlylocase = args.onlylocase
    onlyupcase = args.onlyupcase
    onlysymbols = args.onlysymbols
    if nodigit:
        print(generate_password_no_digit(nodigit))
    if noupcase:
        print(generate_password_no_upcase(noupcase))
    if nolowercase:
        print(generate_password_no_locase(nolowercase))
    if nosymbols:
        print(generate_password_no_symbol(nosymbols))
    if onlydigits:
        print(generate_password_only_digits(onlydigits))
    if onlylocase:
        print(generate_password_only_locase(onlylocase))
    if onlyupcase:
        print(generate_password_only_upcase(onlyupcase))
    if onlysymbols:
        print(generate_password_only_symbols(onlysymbols))


if __name__ == "__main__":
    main()
