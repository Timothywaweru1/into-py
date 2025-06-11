from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Recommended to avoid warning also Disables unnecessary overhead

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/about')
def about():
    return "This is about us page"

@app.route("/<username>")
def username(username):
    return f'Hello {username}!'

if __name__ == '__main__':
    app.run(debug=True, port=5555)