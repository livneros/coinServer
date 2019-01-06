import json

def app(environ, start_response):
    data = json.dumps({
        "response": "ok"
    })
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
