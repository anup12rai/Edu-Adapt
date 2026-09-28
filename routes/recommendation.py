from flask import Blueprint, render_template, request, session
from services.recommendation_service import recommendations
from utils.helper import login_required
bp=Blueprint('recommendation',__name__,url_prefix='/recommendations')
@bp.route('/')
@login_required
def index(): return render_template('recommendations/recommendations.html',items=recommendations(session['user_id'],request.args.get('refresh')=='1'))
