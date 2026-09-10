from datetime import date

WEIGHTS = {'High': 3, 'Medium': 2, 'Low': 1}

def score(task):
    days = (task['due_date'] - date.today()).days if task.get('due_date') else 14
    urgency = 4 if days < 0 else 3 if days <= 1 else 2 if days <= 3 else 1
    return WEIGHTS.get(task.get('priority'), 2) * urgency
