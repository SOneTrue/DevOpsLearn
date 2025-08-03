from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Привет от backend-а и меня!"
                               "\n И всё удачно работает!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
