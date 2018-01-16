from src.soup import get_matches, get_nested_info
from flask import Flask, jsonify
app = Flask(__name__)
import os
import json
import dryscrape


dryscrape.start_xvfb()

def get_from_file(id):
    try:
        os.system("python3 src/soup.py " + str(id) )
    except:
        pass
    return json.load(open("src.json"))

@app.route('/', methods=['GET'])
def template_get_endpoint():
    return jsonify({'status': "ok"})


@app.route("/get", methods=["GET"])
def get_matches_raw():
    return jsonify({"matches": get_matches()})


@app.route("/get/<id>", methods=["GET"])
def get_match_raw(id):
    return jsonify(get_from_file(id))




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
