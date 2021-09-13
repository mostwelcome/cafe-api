from blueprints.cafe import CAFES_BLUEPRINT
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from databases.db import db

app = Flask(__name__)

app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)

app.register_blueprint(CAFES_BLUEPRINT, url_prefix='/cafes')


@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return redirect(url_for('cafes.get_cafes'))


if __name__ == '__main__':
    app.run()
