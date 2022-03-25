from flask import Flask, render_template
import os

app = Flask(__name__)
FORM_URL = os.environ.get("FORM_URL")

@app.route("/")
def home():
    return render_template("index.html", form_url=FORM_URL)

@app.route("/thanks")
def thanks():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
