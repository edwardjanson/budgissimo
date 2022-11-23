from flask import Flask, render_template, session
from flask_session import Session
from controllers.campaigns_controller import campaigns_blueprint
from controllers.accounts_controller import accounts_blueprint
from controllers.platforms_controller import platforms_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.connections_controller import connections_blueprint


app = Flask(__name__)

app.register_blueprint(campaigns_blueprint)
app.register_blueprint(accounts_blueprint)
app.register_blueprint(platforms_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(connections_blueprint)


# Initiate session for Account 1
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    session.clear()
    session["account_id"] = 1
    return render_template('index.html')


@app.route('/access-denied')
def access_denied():
    return render_template('access_denied.html')


if __name__ == '__main__':
    app.run(debug=True)