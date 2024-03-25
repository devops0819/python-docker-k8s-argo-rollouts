from flask import Flask, abort
from prometheus_flask_exporter import PrometheusMetrics
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
    if random.random() < 0.2:  # 20% chance
        abort(500)
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
