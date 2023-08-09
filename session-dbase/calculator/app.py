from flask import Flask, request, Response, jsonify
import prometheus_client
from pymongo import MongoClient
from flask_pymongo import PyMongo
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
from flask_cors import CORS

#app = Flask(__name__)
#mongo = MongoClient('database', 27017)
#db = mongo['website_db']
#hits_collection = db['hits']


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:root@database:27017/admin"
mongo = PyMongo(app)
hits_collection = mongo.db.usage

# Check if the database and collection exist, create them if not
if "usage" not in mongo.db.list_collection_names():
    hits_collection = mongo.db.create_collection("usage")


CORS(app)
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
    hits_collection.update_one({}, {'$inc': {'count': 1}}, upsert=True)
    return ' Welcome to the Simple Calculator - Base Version'

@app.route('/hits')
def get_hits():
    hits_doc = hits_collection.find_one() or {'count': 0}
    return jsonify({'hits': hits_doc['count']})


@app.route('/add', methods=['GET', 'POST'])
def add():
    hits_collection.update_one({}, {'$inc': {'count': 1}}, upsert=True)
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
    hits_collection.update_one({}, {'$inc': {'count': 1}}, upsert=True)
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
    hits_collection.update_one({}, {'$inc': {'count': 1}}, upsert=True)
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
    hits_collection.update_one({}, {'$inc': {'count': 1}}, upsert=True)
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

