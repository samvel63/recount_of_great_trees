from flask import Flask, render_template, json, request
from app.recount_of_great_trees import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    name = request.form['name']
    res = json.loads(name)
    matrix_lin = res["data"]
    d = recount(matrix_lin)
    return json.dumps({'len': d})


if __name__ == '__main__':
    app.run(debug=True)
