from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(order_bp, url_prefix='/orders')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
