from flask import Flask, render_template
from controllers.campaigns_controller import campaigns_blueprint
from controllers.accounts_controller import accounts_blueprint
from controllers.platforms_controller import platforms_blueprint
from controllers.tags_controller import tags_blueprint


app = Flask(__name__)

app.register_blueprint(campaigns_blueprint)
app.register_blueprint(accounts_blueprint)
app.register_blueprint(platforms_blueprint)
app.register_blueprint(tags_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
