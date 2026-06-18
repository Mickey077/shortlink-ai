from flask import Flask, render_template, request

from utils.shortener import generate_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None

    if request.method == "POST":

        original_url = request.form["url"]

        code = generate_code()

        short_url = f"http://127.0.0.1:5000/{code}"

    return render_template(
        "index.html",
        short_url=short_url
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
