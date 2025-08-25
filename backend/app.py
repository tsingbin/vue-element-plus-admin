from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    from .blueprints.department import department_bp
    from .blueprints.user import user_bp
    from .blueprints.role import role_bp
    from .blueprints.menu import menu_bp
    from .blueprints.dict import dict_bp
    from .blueprints.request import request_bp
    from .blueprints.table import table_bp
    from .blueprints.analysis import analysis_bp
    from .blueprints.workplace import workplace_bp
    
    app.register_blueprint(department_bp, url_prefix='/department')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(role_bp, url_prefix='/role')
    app.register_blueprint(menu_bp, url_prefix='/menu')
    app.register_blueprint(dict_bp, url_prefix='/dict')
    app.register_blueprint(request_bp, url_prefix='/request')
    app.register_blueprint(table_bp, url_prefix='/table')
    app.register_blueprint(analysis_bp, url_prefix='/analysis')
    app.register_blueprint(workplace_bp, url_prefix='/workplace')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)
