def generate(risk, overdue, completed, total):
    ideas = []
    if overdue: ideas.append(f'Complete or reschedule your {overdue} overdue task(s) first.')
    if risk >= 60: ideas.append('Your workload risk is high—schedule two focused study blocks today.')
    if total and completed / total < .5: ideas.append('Break your next task into a 25-minute first step to build momentum.')
    if not ideas: ideas.append('You are on track. Protect your progress with a short review session this week.')
    return ideas
