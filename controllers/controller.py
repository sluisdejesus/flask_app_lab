from flask import render_template, request, redirect
from werkzeug.utils import redirect
from app import app
from models.events_list import *
from models.event import Event

@app.route("/events")
def index():
    return render_template ('index.html', title = "Home", events=Events)

@app.route('/events',methods=['POST'])
def add_event():
    date = request.form["date"]
    name_of_event= request.form["name_of_event"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    new_event = Event(date,name_of_event,number_of_guests,room_location,description)
    add_new_event(new_event)

    # return render_template("index.html", title="Home", events=Events)
    return redirect("/events")