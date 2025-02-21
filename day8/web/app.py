from flask import Flask, render_template
import json

app = Flask(__name__)


@app.get("/")
@app.post("/")
def index():
    return render_template("index.html", name="Giovanni")


@app.route("/pessoas/<is_active>")
def pessoas(is_active):
    # is_active = request.args.get("is_active", "true")
    pessoas = get_pessoas(
        is_active=True if is_active.lower() == "active" else False
    )
    return render_template("pessoas.html", pessoas=pessoas)


def get_pessoas(is_active=None):
    data = json.loads(
        open("data.json").read()
    )
    if is_active is not None:
        return [
            pessoa for pessoa in data
            if pessoa["is_active"] == is_active
        ]
