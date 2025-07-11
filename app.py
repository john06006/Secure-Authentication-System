from flask import Flask
from routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from models.database import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
