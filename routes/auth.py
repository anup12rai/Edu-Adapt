from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from services.auth_service import authenticate, register
from utils.validator import valid_email
bp = Blueprint('auth', __name__)

# @bp.route('/')
# def home(): return redirect(url_for('dashboard.index') if session.get('user_id') else url_for('auth.login'))
@bp.route('/')
def home():
    if session.get('user_id'):
        return redirect(url_for('dashboard.index'))

    return render_template('home/home.html')



@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = authenticate(request.form.get('email','').strip().lower(), request.form.get('password',''))
        if user:
            session.clear(); session['user_id']=user['id']; session['user_name']=user['full_name']; return redirect(url_for('dashboard.index'))
        flash('Invalid email or password.', 'danger')
    return render_template('auth/login.html')
@bp.route('/register', methods=['GET','POST'])
def register_view():
    if request.method == 'POST':
        name, email, password = request.form.get('full_name','').strip(), request.form.get('email','').strip().lower(), request.form.get('password','')
        if len(name) < 2 or not valid_email(email) or len(password) < 8: flash('Enter your name, a valid email, and a password of at least 8 characters.', 'danger')
        elif not register(name,email,password): flash('An account with that email already exists.', 'danger')
        else: flash('Account created. Please sign in.', 'success'); return redirect(url_for('auth.login'))
    return render_template('auth/register.html')
@bp.post('/logout')
def logout(): session.clear(); return redirect(url_for('auth.login'))
