from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin
from main import main

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

@app.route('/')
@cross_origin()
def ports():
    return json.dumps(main())

app.run()