from flask import Flask, render_template, json, request
from app.recount_of_great_trees import *
from app.search_great_trees import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    name = request.form['name']
    res = json.loads(name)
    lin_matrix = res["data"]
    graph = to_two_dimensional(lin_matrix)
    root = find_root(graph)
    d = recount(graph, root)
    lst = search_great_trees(len(graph), root, graph, d)
    return json.dumps({'len': d, 'graphs': lst})


if __name__ == '__main__':
    app.run(debug=True)