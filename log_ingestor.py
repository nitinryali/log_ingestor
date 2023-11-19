from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
es = Elasticsearch(['http://localhost:9200'],timeout=30)
executor = ThreadPoolExecutor() 

def ingest_to_elasticsearch(log_data):
    try:
        es.index(index='logs', body=log_data)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        log_data = request.get_json()
        executor.submit(ingest_to_elasticsearch, log_data)
        return jsonify({"status": "accepted"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(port=3000)
