from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "MediSync AI"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)