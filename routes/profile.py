from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from utils.db import execute, query
from utils.helper import login_required
bp=Blueprint('profile',__name__,url_prefix='/profile')
@bp.route('/',methods=['GET','POST'])
@login_required
def index():
    if request.method=='POST':
        name=request.form.get('full_name','').strip()
        if name: execute('UPDATE users SET full_name=%s WHERE id=%s',(name,session['user_id'])); session['user_name']=name; flash('Profile updated.','success')
        return redirect(url_for('profile.index'))
    return render_template('profile/profile.html',user=query('SELECT id,full_name,email,created_at FROM users WHERE id=%s',(session['user_id'],),one=True))
@bp.post('/delete-account')
@login_required
def delete_account():
    execute('DELETE FROM users WHERE id=%s', (session['user_id'],))
    session.clear()
    flash('Your account and all associated learning data were deleted.', 'success')
    return redirect(url_for('auth.login'))
