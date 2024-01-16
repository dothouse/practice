from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views, pension_views, tour_views, office_views, select_views
    from .views import restaurant_views, result_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(pension_views.bp)
    app.register_blueprint(tour_views.bp)
    app.register_blueprint(office_views.bp)
    app.register_blueprint(select_views.bp)
    app.register_blueprint(restaurant_views.bp)
    app.register_blueprint(result_views.bp)

    return app