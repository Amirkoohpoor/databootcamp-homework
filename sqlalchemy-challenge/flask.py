import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates"""
    # Query 
    results = session.query(Measurement.data, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_date
    all_data = []
    for date, prcp in results:
        data_dict = {}
        data_dict["date"] = date
        data_dict["prcp"] = prcp
        all_data.append(data_dict)

    return jsonify(all_data)



@app.route("/api/v1.0/stations")
def Station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates"""
    # Query 
    results2 = session.query(Station.station).all()

    session.close()

    # Create a dictionary from the row data and append to a list
    all_station = []
    for station in results2:
        station_dict = {}
        station_dict["station"] = station

        all_station.append(station_dict)

    return jsonify(all_station)

if __name__ == "__main__":
    app.run(debug=True)

