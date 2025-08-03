import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return f"{os.getenv('GREETING', 'Значение не найдено, или ты криворукий!')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
