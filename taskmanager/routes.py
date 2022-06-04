from flask import render_template
from taskmanager import app, db  # noqa
from taskmanager.models import Category, Task


@app.route("/")
def home():
    ''' Lunch HTML base file '''
    return render_template("tasks.html")
