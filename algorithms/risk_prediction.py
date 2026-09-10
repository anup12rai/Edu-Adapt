def predict(completion, overdue, study_minutes):
    risk = (100 - completion) * .5 + min(overdue * 12, 36) - min(study_minutes / 30, 20)
    return max(0, min(100, round(risk)))
