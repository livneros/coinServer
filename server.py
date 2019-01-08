import json
import flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/', methods=['POST', 'GET'])
def run():
    if request.method == 'GET':
        return "hello world"
    print("request: ", request)
    data = json.dumps({
        "email": request.args.get("email"),
        "content": request.args.get("content")
    })
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
