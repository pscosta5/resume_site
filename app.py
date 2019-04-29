from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/communication")
def communication():
    return render_template(("communication.html"))


if __name__ == "__main__":
    app.run(debug=False)
