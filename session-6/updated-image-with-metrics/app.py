from flask import Flask, request, Response
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app = Flask(__name__)

_INF = float("inf")


graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

@app.route('/')
def home():
    start = time.time()
    graphs['c'].inc()
    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return ' Welcome to the Simple Calculator - Base Version'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')

    result = float(num1) + float(num2)
    return {'result': result}

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    if request.method == 'POST':
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')

    result = float(num1) - float(num2)
    return {'result': result}

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')

    result = float(num1) * float(num2)
    return {'result': result}

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'POST':
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')

    result = float(num1) / float(num2)
    return {'result': result}

@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

