from algorithms.simulation_engine import simulate
from services.dashboard_service import summary
from utils.db import execute, query

def run(user_id, expected_gpa):
    progress = summary(user_id)
    gpa, score = simulate(expected_gpa, progress['readiness'])
    execute('INSERT INTO simulations (user_id,expected_gpa,predicted_score) VALUES (%s,%s,%s)', (user_id,gpa,score))
    return {'target': gpa, 'likelihood': score, 'readiness': progress['readiness'], 'completed': progress['completed'], 'total': progress['total'], 'completion': progress['completion']}
def history(user_id): return query('SELECT * FROM simulations WHERE user_id=%s ORDER BY created_at DESC LIMIT 10', (user_id,))
