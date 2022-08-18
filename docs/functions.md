# Functions 
- generate_password_all
```Python
def generate_password_all(MAX_LEN: int) -> str:
    """
    The generate_password_all function generates a password of the length specified by MAX_LEN.
    The password is generated using the following characters: digits, uppercase letters, lowercase letters and symbols.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Determine the length of the password

    Returns:
        A string of randomly generated characters
    """
```


- generate_password_no_digit
```Python
    """
    The generate_password_no_digit function generates a password that does not contain any digits.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Determine the length of the password

    Returns:
        A string of characters that is the length of max_len
    """
```

- generate_password_no_upcase
```Python
    """
    The generate_password_no_upcase function generates a password of the desired length,
    without any uppercase characters. The function takes one argument, MAX_LEN (an integer),
    and returns a string.

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password
    """
```

- generate_password_no_locase
```Python
    """
    The generate_password_no_locase function generates a password that is comprised of digits, uppercase characters, and symbols. The function takes one argument: MAX_LEN (an integer). It then generates a random digit from the DIGITS list using the random.choice() function. It also chooses a random character from the UPCASE_CHARACTERS list using another call to random.choice(). Lastly it chooses a symbol from SYMBOLS and appends all three of these randomly generated characters to form an initial temporary password string called temp_pass.

    The for loop iterates over range(MAX_LEN - 4) which means that it

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password that is
    """
```
- generate_password_no_symbol

```Python
    """
    The generate_password_no_symbol function generates a password with no symbols.
    It takes one parameter, MAX_LEN, which is the maximum length of the password.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Define the maximum length of the password

    Returns:
        A password with no symbols
    """
```

- generate_password_only_digits
```Python
    """
    The generate_password_only_digits function generates a password that is only comprised of digits.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is a combination of digits with no special characters
    """
```

- generate_password_only_upcase
```Python
    """
    The generate_password_only_upcase function generates a password that is only comprised of uppercase characters.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is only comprised of uppercase characters
    """
```

- generate_password_only_locase
```Python
    """
    The generate_password_only_locase function generates a password that is comprised of only lowercase characters.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Specify the maximum length of the password

    Returns:
        A password that is all lowercase letters
    """
```

- generate_password_only_symbols
```Python
    """
    The generate_password_only_symbols function generates a password that is comprised of only symbols.
    The function takes one argument, MAX_LEN, which is the maximum length of the password to be generated.
    The function returns a string containing the randomly generated password.

    Args:
        MAX_LEN:int: Set the maximum length of the password

    Returns:
        A password that is
    """
```
