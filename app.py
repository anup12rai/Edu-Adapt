from flask import Flask
from config import Config
<<<<<<< HEAD
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
=======
from utils.db import init_app


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    init_app(app)

    from routes.auth import bp as auth_bp
    from routes.dashboard import bp as dashboard_bp
    from routes.subject import bp as subject_bp
    from routes.planner import bp as planner_bp
    from routes.task import bp as task_bp
    from routes.calendar import bp as calendar_bp
    from routes.pomodoro import bp as pomodoro_bp
    from routes.analytics import bp as analytics_bp
    from routes.recommendation import bp as recommendation_bp
    from routes.simulation import bp as simulation_bp
    from routes.reflection import bp as reflection_bp
    from routes.notification import bp as notification_bp
    from routes.profile import bp as profile_bp
    for blueprint in (auth_bp, dashboard_bp, subject_bp, planner_bp, task_bp, calendar_bp,
                      pomodoro_bp, analytics_bp, recommendation_bp, simulation_bp,
                      reflection_bp, notification_bp, profile_bp):
        app.register_blueprint(blueprint)
    @app.context_processor
    def sidebar_data():
        from flask import session
        if session.get('user_id'):
            from services.dashboard_service import sidebar, summary
            return {'side_summary': summary(session['user_id']), 'side_data': sidebar(session['user_id'])}
        return {}
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
>>>>>>> 1650dd9 (eduadapt project)
