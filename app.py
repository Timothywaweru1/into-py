from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions (but don't connect to app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import models after db is initialized to avoid circular imports
    from models import User

    @app.route('/')
    def index():
        return "Hello world!"

    @app.route('/about')
    def about():
        return "This is about us page"

    @app.route("/<username>")
    def username(username):
        return f'Hello {username}!'

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5555)