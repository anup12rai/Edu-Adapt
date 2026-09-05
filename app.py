from flask import Flask
from flask_cors import CORS

from config import Config
from models import db

# Import Models
from models.user import User
from models.subject import Subject
from models.unit import Unit
from models.task import Task
from models.study_session import StudySession
from models.notification import Notification
from models.reflection import Reflection
from models.simulation import Simulation
from models.recommendation import Recommendation

# Import Blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.subject import subjects_bp
from routes.planner import planner_bp
from routes.calendar import calendar_bp
from routes.analytics import analytics_bp
from routes.simulation import simulation_bp
from routes.notification import notification_bp
from routes.profile import profile_bp
from routes.recommendation import recommendation_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
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

    # Home Route
    @app.route("/")
    def home():
        return {
            "success": True,
            "application": "EduAdapt",
            "version": "1.0",
            "message": "EduAdapt Backend Running Successfully"
        }

    # Health Check
    @app.route("/api/test")
    def test():
        return {
            "success": True,
            "message": "API Connected Successfully"
        }

    # 404 Handler
    @app.errorhandler(404)
    def not_found(error):
        return {
            "success": False,
            "message": "Endpoint Not Found"
        }, 404

    # 500 Handler
    @app.errorhandler(500)
    def server_error(error):
        return {
            "success": False,
            "message": "Internal Server Error"
        }, 500

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )