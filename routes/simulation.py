<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from models import db
from models.simulation import Simulation

simulation_bp = Blueprint(
    "simulation",
    __name__,
    url_prefix="/api/simulation"
)


@simulation_bp.route("/", methods=["POST"])
def create_simulation():

    data = request.get_json()

    expected_gpa = float(data.get("expected_gpa", 0))
    predicted_score = expected_gpa * 20

    simulation = Simulation(
        user_id=data.get("user_id"),
        expected_gpa=expected_gpa,
        predicted_score=predicted_score
    )

    db.session.add(simulation)
    db.session.commit()

    return jsonify({
        "success": True,
        "expected_gpa": expected_gpa,
        "predicted_score": predicted_score
    })
=======
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
>>>>>>> 1650dd9 (eduadapt project)
