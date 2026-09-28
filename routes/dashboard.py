from flask import Blueprint, render_template, session
from services.dashboard_service import summary
from services.planner_service import plan
from utils.helper import login_required
bp=Blueprint('dashboard',__name__,url_prefix='/dashboard')
@bp.route('/')
@login_required
def index(): return render_template('dashboard/dashboard.html', summary=summary(session['user_id']), plan=plan(session['user_id'])[:3])
