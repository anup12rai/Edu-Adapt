from flask import Blueprint, redirect, render_template, session, url_for
from services.notification_service import all_for, mark_read
from utils.helper import login_required
bp=Blueprint('notification',__name__,url_prefix='/notifications')
@bp.route('/')
@login_required
def index(): return render_template('notifications/notifications.html',items=all_for(session['user_id']))
@bp.post('/read-all')
@login_required
def read_all(): mark_read(session['user_id']); return redirect(url_for('notification.index'))
