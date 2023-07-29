
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify, render_template
from kids import analyzeCodeKids
from analyze import analyzeCode

app = Flask(__name__)

# A poor mans scheme to support deploying to a production server by simply copying the template files and replacing api keys.
LOCAL=True
suffix=""
if LOCAL:
    suffix="local"

# UI endpoints
################
#@app.route('/test')
#def index():
#    return render_template('index' + suffix + '.html')

@app.route('/')
def kids():
    return render_template('kids' + suffix + '.html')

# API endpoints
################
@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json.get('code')
    hints = analyzeCode(code)
    return jsonify({'hints': hints})

@app.route('/analyzekids', methods=['POST'])
def analyzedev():
    code = request.json.get('code')
    hints = analyzeCodeKids(code)
    return jsonify({'hints': hints})

# Debugging end points
################################
@app.route('/healthz', methods=['GET', 'POST'])
def healthy():
    return 'OK\n'

@app.route('/help', methods=['GET', 'POST'])
def helpy():
    return 'curl -X POST -H "Content-Type: application/json" -d \'{"code": "print(\\\"Hello, world\\\")"}\' http://localhost:5000/analyze\n'

@app.route('/echo', methods=['POST'])
def debug():
    return request.json

