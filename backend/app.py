from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os

app = Flask(__name__)

# Метрика — счётчик HTTP-запросов
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Общее количество HTTP-запросов',
    ['method', 'endpoint']
)

@app.route('/')
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return f"{os.getenv('GREETING', 'Значение не найдено, или ты криворукий!')}"

# Endpoint для метрик
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
