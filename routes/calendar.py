from flask import Blueprint, render_template, send_file, session
from utils.db import query
from utils.helper import login_required
bp=Blueprint('calendar',__name__,url_prefix='/calendar')
@bp.route('/')
@login_required
def index(): return render_template('calendar/calendar.html',tasks=query('SELECT * FROM tasks WHERE user_id=%s AND due_date IS NOT NULL ORDER BY due_date',(session['user_id'],)))
@bp.route('/download/<int:days>')
@login_required
def download(days):
    if days not in (7,30): days=7
    from services.export_service import build_plan_pdf
    return send_file(build_plan_pdf(session['user_id'],days),as_attachment=True,download_name=f'eduapt-{days}-day-plan.pdf',mimetype='application/pdf')
