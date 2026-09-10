"""Built-in starter catalogue; users can always edit or add their own subjects."""
from services.subject_service import add_topic, add_unit, create
from utils.db import query

TU_BCA_4 = [
 ('Operating System', 3, 'High', [('Introduction and Process Management',['OS services','Processes and threads','CPU scheduling']),('Memory and Storage',['Memory management','Virtual memory','File systems']),('Protection',['Deadlocks','Security and protection'])]),
 ('Numerical Methods', 3, 'Medium', [('Errors and Roots',['Error analysis','Bisection method','Newton-Raphson method']),('Interpolation',['Finite differences','Newton interpolation','Lagrange interpolation']),('Numerical Calculus',['Numerical differentiation','Numerical integration','Differential equations'])]),
 ('Software Engineering', 3, 'High', [('Software Process',['Process models','Agile development','Requirements engineering']),('Design and Quality',['Architectural design','Testing strategies','Software quality']),('Project Management',['Estimation','Scheduling','Risk management'])]),
 ('Scripting Language', 3, 'Medium', [('Python Fundamentals',['Syntax and data types','Control flow','Functions and modules']),('Web and Data',['File handling','Web scripting','Database connectivity']),('Advanced Concepts',['Object-oriented programming','Exception handling','Regular expressions'])]),
 ('Database Management System', 3, 'High', [('Database Foundations',['Database architecture','ER modelling','Relational model']),('SQL and Design',['SQL queries','Normalization','Transaction management']),('Advanced DBMS',['Indexing','Recovery','Distributed databases'])]),
 ('Project I', 3, 'Medium', [('Project Planning',['Problem identification','Proposal writing','Requirements gathering']),('Implementation',['Design','Prototype development','Documentation'])]),
]

def import_tu_bca_fourth(user_id):
    count = 0
    for name, credits, priority, units in TU_BCA_4:
        if query('SELECT id FROM subjects WHERE user_id=%s AND subject_name=%s', (user_id, name), one=True):
            continue
        subject_id = create(user_id, name, credits, priority)
        for unit_name, topics in units:
            unit_id = add_unit(subject_id, unit_name)
            for topic in topics: add_topic(unit_id, topic)
        count += 1
    return count
