from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
es = Elasticsearch(['http://localhost:9200'],timeout=30)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['GET'])
def query_logs():
    try:
        query_params = {field: request.args.get(field) for field in request.args}
        query_body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {field: value}} for field, value in query_params.items() if value
                    ]
                }
            }
        }
        result = es.search(index='logs', body=query_body)
        return jsonify({"status": "success", "data": result['hits']['hits']})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(port=4000) 
