import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# In order to actually use any of our hidden environment variables, we 
# to import the 'env' package.
# However, since we are not pushing the env.py file to GitHub, this file
# will not be visible once deployed to Heroku, and will throw an error.
# This is why we need to only import 'env' if the OS can find an existing
# file path for the env.py file itself.
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri #heroku


db = SQLAlchemy(app)

from taskmanager import routes  # noqa