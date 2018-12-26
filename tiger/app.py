from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/slider")
def slider():
    return render_template("slider.html")

@app.route("/swiper")
def swiper():
    return render_template("swiper.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9099, debug=True)
