from flask import Flask
from config import Config
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
