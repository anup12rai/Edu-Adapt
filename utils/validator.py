import re


def validate_email(email):
    """
    Validate email address.
    """

    if not email:
        return False

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))


def validate_password(password):
    """
    Basic password validation.
    """

    if not password:
        return False

    return len(password) >= 6


def validate_required(data, fields):
    """
    Check whether required fields exist.
    """

    missing = []

    for field in fields:
        if field not in data or data[field] in (None, ""):
            missing.append(field)

    return missing


def validate_positive_number(value):
    try:
        return float(value) >= 0
    except (ValueError, TypeError):
        return False