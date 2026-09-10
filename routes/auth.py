<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from models import db
from models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")

    if not full_name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required"
        }), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 409

    user = User(
        full_name=full_name,
        email=email,
        password=password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Registration successful",
        "user_id": user.id
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(
        email=email,
        password=password
    ).first()

    if not user:
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 401

    return jsonify({
        "success": True,
        "message": "Login successful",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email
        }
    })
=======
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from services.auth_service import authenticate, register
from utils.validator import valid_email
bp = Blueprint('auth', __name__)

@bp.route('/')
def home(): return redirect(url_for('dashboard.index') if session.get('user_id') else url_for('auth.login'))
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
>>>>>>> 1650dd9 (eduadapt project)
