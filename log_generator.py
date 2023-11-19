import requests
import json
import random
import time

log_ingestor_url = "http://localhost:3000/ingest"

def generate_log_entry():
    log_levels = ["info", "warning", "error"]
    resource_ids = ["server-1234", "server-5678", "server-9012"]
    trace_id = "xyz-" + str(random.randint(100, 999)) + "-123"
    span_id = "span-" + str(random.randint(100, 999))
    commit = "{:06x}".format(random.randint(0, 0xFFFFFF))
    parent_resource_id = "server-" + str(random.randint(1000, 9999))

    log_entry = {
        "level": random.choice(log_levels),
        "message": f"Log message for {trace_id}",
        "resourceId": random.choice(resource_ids),
        "timestamp": "2023-09-15T{}:{}:00Z".format(random.randint(0, 23), random.randint(0, 59)),
        "traceId": trace_id,
        "spanId": span_id,
        "commit": commit,
        "metadata": {
            "parentResourceId": parent_resource_id
        }
    }

    return log_entry

def send_log_entry(log_entry):
    try:
        response = requests.post(log_ingestor_url, json=log_entry)
        if response.status_code == 200:
            print(f"Log entry successfully sent: {log_entry}")
        else:
            print(f"Failed to send log entry. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending log entry: {str(e)}")

if __name__ == "__main__":
    for _ in range(10): 
        log_data = generate_log_entry()
        send_log_entry(log_data)
        time.sleep(1) 
