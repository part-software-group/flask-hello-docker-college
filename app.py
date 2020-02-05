from flask import Flask, jsonify, request
import os


app = Flask(__name__)
methods = ["GET", "POST", "PATCH", "DELETE"]
name = os.environ['NAME']

@app.route("/", methods=methods, defaults={"path": ""})
@app.route("/<path:path>", methods=methods)
def hello_world(path):

    return jsonify(
        {
            "endpoint": path,
            "name" : name
        }
    )


if __name__ == "__main__":
    app.run()
