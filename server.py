import flask
from flask import json

app = flask.Flask(__name__)


@app.route("/")
def library_home():
    return flask.render_template('library_home.html')


@app.route('/add-book', methods=['GET','POST'])
def add_book():
    if flask.request.method == "GET":
        return flask.render_template('add_book.html')
    if flask.request.method == "POST":
        input_request = flask.request.form
        print(input_request)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/library')
def library():
    return flask.render_template('library.html')


if __name__ == "__main__":
    app.run(debug=True)
