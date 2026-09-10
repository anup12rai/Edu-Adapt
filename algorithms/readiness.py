def calculate(completed, total, completion):
    task_rate = (completed / total * 100) if total else 0
    return round(task_rate * .55 + completion * .45)
