from flask import Blueprint, flash, redirect, render_template, session, url_for
from services.planner_service import completed_today, generate_today, has_today_plan, plan
from utils.helper import login_required
bp=Blueprint('planner',__name__,url_prefix='/planner')
@bp.route('/')
@login_required
def index(): return render_template('planner/planner.html', plan=plan(session['user_id']), done=completed_today(session['user_id']), generated=has_today_plan(session['user_id']))
@bp.post('/generate')
@login_required
def generate():
    created = generate_today(session['user_id'])
    flash(f'{created} study tasks added to today\'s plan.' if created else 'Complete today\'s plan before generating another one.', 'success' if created else 'warning')
    return redirect(url_for('planner.index'))
