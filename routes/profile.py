<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from models import db
from models.user import User

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/api/profile"
)


@profile_bp.route("/<int:user_id>", methods=["GET"])
def get_profile(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    return jsonify({
        "success": True,
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "created_at": str(user.created_at)
        }
    })


@profile_bp.route("/<int:user_id>", methods=["PUT"])
def update_profile(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    data = request.get_json()

    user.full_name = data.get(
        "full_name",
        user.full_name
    )

    user.email = data.get(
        "email",
        user.email
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Profile updated successfully"
    })
=======
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
>>>>>>> 1650dd9 (eduadapt project)
