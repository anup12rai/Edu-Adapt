import re


def valid_email(value):
    return bool(re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', value or ''))


def one_of(value, options, default):
    return value if value in options else default
