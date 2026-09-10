from algorithms.priority_algorithm import score

def build_plan(tasks, limit=5):
    ordered = sorted(tasks, key=score, reverse=True)
    minutes = {'High': 45, 'Medium': 35, 'Low': 25}
    return [{'task': t, 'suggested_minutes': minutes.get(t.get('priority'), 35)} for t in ordered[:limit]]
