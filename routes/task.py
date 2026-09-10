from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from utils.db import execute, query
from utils.helper import login_required
from utils.validator import one_of
bp=Blueprint('task',__name__,url_prefix='/tasks')
@bp.route('/',methods=['GET','POST'])
@login_required
def index():
    uid=session['user_id']
    if request.method=='POST':
        execute('INSERT INTO tasks (user_id,title,description,due_date,priority) VALUES (%s,%s,%s,%s,%s)',(uid,request.form['title'].strip(),request.form.get('description','').strip() or None,request.form.get('due_date') or None,one_of(request.form.get('priority'),{'Low','Medium','High'},'Medium'))); flash('Task added.','success'); return redirect(url_for('task.index'))
    tasks=query('SELECT * FROM tasks WHERE user_id=%s ORDER BY status, due_date IS NULL, due_date',(uid,))
    return render_template('tasks/tasks.html',tasks=tasks)
@bp.post('/<int:task_id>/toggle')
@login_required
def toggle(task_id):
    execute("UPDATE tasks SET status=IF(status='Completed','Pending','Completed') WHERE id=%s AND user_id=%s",(task_id,session['user_id'])); return redirect(request.referrer or url_for('planner.index'))
@bp.post('/<int:task_id>/delete')
@login_required
def delete(task_id): execute('DELETE FROM tasks WHERE id=%s AND user_id=%s',(task_id,session['user_id'])); flash('Task deleted.','success'); return redirect(url_for('task.index'))
