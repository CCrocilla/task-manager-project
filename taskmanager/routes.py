from flask import render_template
from taskmanager import app, db  # noqa


@app.route("/")
def home():
    ''' Lunch HTML base file '''
    return render_template("base.html")