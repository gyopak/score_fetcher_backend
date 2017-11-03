from flask import Flask, jsonify
import json
from logger import log, get_log_messages
from src.fetcher import get_raw
app = Flask(__name__)


@app.route('/', methods=['GET'])
def template_get_endpoint():
    log("endpoint visited")
    return jsonify({'status': "ok"})


@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(get_log_messages())

@app.route("/get", methods=["GET"])
def get_raw_data():
    return str(get_raw())

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
