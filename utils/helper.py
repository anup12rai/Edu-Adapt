from datetime import datetime, date


def success_response(message="Success", data=None):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message="Something went wrong"):
    return {
        "success": False,
        "message": message,
        "data": None
    }


def calculate_percentage(completed, total):
    """
    Calculate completion percentage.
    """

    if total == 0:
        return 0

    return round((completed / total) * 100, 2)


def calculate_remaining_days(deadline):
    """
    Calculate number of days remaining until deadline.
    """

    if not deadline:
        return None

    if isinstance(deadline, str):
        deadline = datetime.strptime(
            deadline,
            "%Y-%m-%d"
        ).date()

    today = date.today()

    return (deadline - today).days


def format_date(value):
    """
    Convert date/datetime to YYYY-MM-DD.
    """

    if isinstance(value, (datetime, date)):
        return value.strftime("%Y-%m-%d")

    return value


def clamp(value, minimum, maximum):
    """
    Keep a number between minimum and maximum.
    """

    return max(minimum, min(value, maximum))


def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default