from src.soup import get_matches, get_match
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def template_get_endpoint():
    return jsonify({'status': "ok"})


@app.route("/get", methods=["GET"])
def get_matches_raw():
    return jsonify(get_matches())


@app.route("/get/<id>", methods=["GET"])
def get_match_raw(id):
    return jsonify(get_match(id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
