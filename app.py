"""Web app."""
import flask

app = flask.Flask(__name__)


@app.route("/")
def index() -> str:
    """Base page."""
    return flask.render_template("layout.html")


@app.route("/about")
def about() -> str:
    """Route to about page."""
    return flask.render_template("about.html")


@app.route("/projects")
def projects() -> str:
    """Route to projects page."""
    return flask.render_template("projects.html")


@app.route("/communication")
def communication() -> str:
    """Route to communication page."""
    return flask.render_template(("communication.html"))


if __name__ == "__main__":
    app.run(debug=False)
