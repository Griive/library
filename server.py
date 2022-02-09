import flask as flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def library_home():
    return flask.render_template('library_home.html')

@app.route('/add_position')
def add_position():
    return flask.render_template('add_position.html')

@app.route('/library')
def library():
    return flask.render_template('library.html')


if __name__ == "__main__":
    app.run()