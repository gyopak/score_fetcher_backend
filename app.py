from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def template_get_endpoint():
    return jsonify({'status': "ok"})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
