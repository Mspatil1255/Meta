from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({"status": "success"}), 200

@app.route("/validate", methods=["POST"])
def validate():
    return jsonify({"status": "success"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
