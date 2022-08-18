#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

from psgen.funcs import *


def hello_test():
    """
    This defines the expected usage, which can then be used in various test cases.
    Pytest will not execute this code directly, since the function does not contain the suffex "test"
    """
    generate_password_all(12)


def test_gen_all(unit_test_mocks: None):
    """
    Simple test to test the `generate_password_all` function
    """
    generate_password_all(12)


def test_gen_no_digit():
    """
    Test no digit function
    """
    generate_password_no_digit(12)


def test_gen_no_upcase():
    """
    Test no digit function
    """
    generate_password_no_upcase(12)


def test_gen_no_locase():
    """
    Test no digit function
    """
    generate_password_no_locase(12)


def test_gen_no_symbol():
    """
    Test no digit function
    """
    generate_password_no_symbol(12)


def test_gen_only_digit():
    """
    Test no digit function
    """
    generate_password_only_digits(12)


def test_gen_only_upcase():
    """
    Test no digit function
    """
    generate_password_only_upcase(12)


def test_gen_only_lowcase():
    """
    Test no digit function
    """
    generate_password_only_locase(12)


def test_gen_only_symbol():
    """
    Test no digit function
    """
    generate_password_only_symbols(12)
