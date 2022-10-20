import datetime

import flask

import services

# create the Flask app
app = flask.Flask(__name__)


@app.route("/")
def library_home():
    return flask.render_template('library_home.html')


@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if flask.request.method == "GET":
        return flask.render_template('add_book.html')
    if flask.request.method == "POST":
        input_request = flask.request.form
        # check book year is integer
        print(input_request)
        # проверка ключа
        if 'bookYear' in input_request.keys() and \
                'bookName' in input_request.keys() and \
                'bookAuthor' in input_request.keys():
            # проверка типа первого парам вторым
            if int(input_request['bookYear']) < datetime.datetime.now().year + 1:
                new_book = services.add_new_book(
                    name=input_request['bookName'],
                    author=input_request['bookAuthor'],
                    year=input_request['bookYear']
                )
                return flask.json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        return flask.json.dumps({'success': False}), 400, {'ContentType': 'application/json'}


@app.route('/library')
def library():
    return flask.render_template('library.html')


# run app in debug mode
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
