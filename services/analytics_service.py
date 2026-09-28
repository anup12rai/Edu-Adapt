from utils.db import query

def analytics(user_id):
    subjects = query("SELECT s.subject_name, COALESCE(SUM(ss.duration),0) minutes FROM subjects s LEFT JOIN study_sessions ss ON ss.subject_id=s.id AND ss.user_id=%s WHERE s.user_id=%s GROUP BY s.id ORDER BY minutes DESC", (user_id,user_id))
    weekly = query("SELECT DATE(session_date) day, SUM(duration) minutes FROM study_sessions WHERE user_id=%s AND session_date >= DATE_SUB(CURDATE(), INTERVAL 6 DAY) GROUP BY DATE(session_date) ORDER BY day", (user_id,))
    risk_rows = query("""SELECT s.subject_name, COALESCE(AVG(u.completion),0) completion
       FROM subjects s LEFT JOIN units u ON u.subject_id=s.id LEFT JOIN tasks t ON t.user_id=s.user_id
       WHERE s.user_id=%s GROUP BY s.id""", (user_id,))
    for row in risk_rows:
        row['risk'] = 'High' if row['completion'] < 35 else 'Medium' if row['completion'] < 70 else 'Low'
        row['recommendation'] = 'Schedule a focused block today' if row['risk'] == 'High' else 'Keep steady weekly progress'
    return {'subjects': subjects, 'weekly': weekly, 'risks': risk_rows}
