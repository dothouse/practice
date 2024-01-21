from flask import Flask

### sql 부분
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    
    ### sql 부분
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #blueprint
    from .views import main_views, select_views, info_views, pension_info_views
    from .views import result_views
    #filter
    from .filter import thousand_comma
    app.jinja_env.filters['t_comma'] = thousand_comma

    app.register_blueprint(main_views.bp)
    app.register_blueprint(select_views.bp)
    app.register_blueprint(info_views.bp)
    app.register_blueprint(pension_info_views.bp)
    app.register_blueprint(result_views.bp)

    return app

