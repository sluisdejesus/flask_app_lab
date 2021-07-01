from flask import Flask
from flask.templating import render_template
from app import app
from models.events_list import Events

@app.route("/events")
def index():
    return render_template ('index.html', title = "Home", events=Events)