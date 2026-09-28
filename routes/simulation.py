from flask import Blueprint, flash, render_template, request, session
from services.simulation_service import history, run
from utils.helper import login_required
bp=Blueprint('simulation',__name__,url_prefix='/simulation')
@bp.route('/',methods=['GET','POST'])
@login_required
def index():
    result=None
    if request.method=='POST':
        try: result=run(session['user_id'],request.form.get('expected_gpa',0))
        except ValueError: flash('Enter a numeric GPA.','danger')
    return render_template('simulation/simulation.html',result=result,history=history(session['user_id']))
