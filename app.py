from flask import Flask, abort
from prometheus_flask_exporter import PrometheusMetrics
import random

app = Flask(__name__)

# Initialize Prometheus metrics exporter for Flask app
metrics = PrometheusMetrics(app)

# Static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
    # Decide whether to return an error or the normal response
    if random.random() < 0.2:  # 20% chance
        abort(500)  # HTTP 500 Internal Server Error
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
