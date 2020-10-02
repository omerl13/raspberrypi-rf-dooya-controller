from transmitter import transmit
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/multi')
def index_multi():
    return render_template('multi.html')


@app.route('/ctrl')
def ctrl():
    requested_code = request.args.get('name')
    transmit([requested_code])
    return requested_code


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
