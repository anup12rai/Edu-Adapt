def simulate(expected_gpa, readiness):
    """Return an explainable likelihood, not a grade prediction."""
    expected = max(0, min(float(expected_gpa), 4.0))
    readiness = max(0, min(float(readiness), 100))
    target_difficulty = (4 - expected) / 4 * 15
    likelihood = round(min(95, max(5, 20 + readiness * .65 + target_difficulty)), 1)
    return expected, likelihood
