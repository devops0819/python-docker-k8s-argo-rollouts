from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Initialize Prometheus metrics exporter for Flask app
metrics = PrometheusMetrics(app)

# Static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
