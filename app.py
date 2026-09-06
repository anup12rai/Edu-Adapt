from flask import Flask
from config import Config
from models import db

# Import models so SQLAlchemy knows about all tables
from models.user import User
from models.subject import Subject
from models.unit import Unit
from models.task import Task
from models.study_session import StudySession
from models.notification import Notification
from models.reflection import Reflection
from models.simulation import Simulation
from models.recommendation import Recommendation

# Import routes
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.subject import subjects_bp
from routes.planner import planner_bp
from routes.calander import calendar_bp
from routes.analytics import analytics_bp
from routes.simulation import simulation_bp
from routes.notification import notification_bp
from routes.profile import profile_bp
from routes.recommendation import recommendation_bp


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(subjects_bp)
app.register_blueprint(planner_bp)
app.register_blueprint(calendar_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(simulation_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(recommendation_bp)


@app.route("/")
def home():
    return """
    <h1>EduAdapt</h1>
    <p>EduAdapt Backend is Running Successfully!</p>
    <p>Flask + MySQL Connected</p>
    """
@app.route("/api/test")
def test():
    return {
        "success": True,
        "message": "EduAdapt API is working!"
    }


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)