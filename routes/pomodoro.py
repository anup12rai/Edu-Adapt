from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from services.pomodoro_service import record
from utils.helper import login_required
bp=Blueprint('pomodoro',__name__,url_prefix='/pomodoro')
@bp.route('/')
@login_required
def index():
    from services.subject_service import subjects
    return render_template('pomodoro/pomodoro.html', subjects=subjects(session['user_id']))
@bp.post('/complete')
@login_required
def complete():
    minutes=max(1,min(180,int(request.form.get('minutes',25))))
    record(session['user_id'],request.form.get('subject_id',type=int),minutes); flash(f'{minutes} study minutes recorded.','success'); return redirect(request.referrer or url_for('dashboard.index'))
