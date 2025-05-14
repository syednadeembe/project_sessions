from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Simple Calculator!'

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

