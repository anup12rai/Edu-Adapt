from flask import Blueprint, render_template, session
from services.analytics_service import analytics
from services.dashboard_service import summary
from utils.helper import login_required
bp=Blueprint('analytics',__name__,url_prefix='/analytics')
@bp.route('/')
@login_required
def index(): return render_template('analytics/analytics.html',data=analytics(session['user_id']),summary=summary(session['user_id']))
