from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("v2/index.html")


@app.route("/day-<num>")
def day(num):
    return render_template("day-" + num + ".html")

@app.route("/exhibit-<num>")
def exhibit(num):
    return render_template("v2/exhibit-" + num + ".html")


@app.route("/qr-<num>")
def qr(num):
    return render_template("qr-" + num + ".html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)