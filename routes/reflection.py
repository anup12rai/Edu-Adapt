from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from services.reflection_service import all_for, create
from utils.helper import login_required
bp=Blueprint('reflection',__name__,url_prefix='/reflections')
@bp.route('/',methods=['GET','POST'])
@login_required
def index():
    if request.method=='POST': create(session['user_id'],request.form.get('notes','').strip(),request.form.get('mood','').strip()); flash('Reflection saved.','success'); return redirect(url_for('reflection.index'))
    return render_template('reflections/reflections.html',items=all_for(session['user_id']))
