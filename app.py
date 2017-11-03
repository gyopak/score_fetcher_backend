from flask import Flask, jsonify
import json
from src.logger import log, get_log_messages
from src.fetcher import get_teams
app = Flask(__name__)


@app.route('/', methods=['GET'])
def template_get_endpoint():
    log("endpoint visited")
    return jsonify({'status': "ok"})


@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(get_log_messages())

@app.route("/teams", methods=["GET"])
def get_raw_teams():
    teams = str(get_teams())
    return str(len(teams))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
