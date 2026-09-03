from datetime import date, timedelta


def generate_dates(start_date, number_of_days):
    """
    Generate a list of dates.
    """

    dates = []

    for i in range(number_of_days):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date)

    return dates


def distribute_hours(total_hours, number_of_days):
    """
    Distribute study hours across available days.
    """

    if number_of_days <= 0:
        return []

    base_hours = total_hours / number_of_days

    return [round(base_hours, 2)] * number_of_days


def calculate_daily_capacity(available_hours):
    """
    Return usable study hours.

    Keeps some time available for breaks and other activities.
    """

    if available_hours <= 0:
        return 0

    return round(available_hours * 0.9, 2)


def prioritize_tasks(tasks):
    """
    Sort tasks according to priority, deadline and difficulty.
    """

    def score(task):

        priority = task.get("priority", 1)
        difficulty = task.get("difficulty", 1)
        remaining_days = task.get("remaining_days", 999)

        deadline_score = 1000 / max(remaining_days + 1, 1)

        return (
            priority * 10
            + difficulty * 5
            + deadline_score
        )

    return sorted(
        tasks,
        key=score,
        reverse=True
    )


def generate_study_plan(tasks, available_hours):
    """
    Generate a simple adaptive study plan.

    Each task should contain:
        estimated_hours
        priority
        difficulty
        remaining_days
    """

    if available_hours <= 0:
        return []

    tasks = prioritize_tasks(tasks)

    plan = []
    remaining_hours = available_hours

    for task in tasks:

        estimated_hours = float(
            task.get("estimated_hours", 1)
        )

        if remaining_hours <= 0:
            break

        allocated = min(
            estimated_hours,
            remaining_hours
        )

        plan.append({
            "task_id": task.get("id"),
            "title": task.get("title"),
            "allocated_hours": round(allocated, 2),
            "priority": task.get("priority", 1),
            "difficulty": task.get("difficulty", 1)
        })

        remaining_hours -= allocated

    return plan