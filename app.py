from flask import Flask, jsonify, request
from data import FlightData

app = Flask(__name__)
flight_data = FlightData('sqlite:///data/flights.sqlite3')


@app.route("/", methods=["GET"])
def home():
    message = """ 
    Welcome to the flights API
    You have the following routes available:
    1. /flights/&lt;int:flight_id&gt;
    2. /flights/delayed/&lt;string:airline_name&gt; 
    3. /flights/delayed/airport/&lt;string:airport_iata&gt;
    4. /flights/&lt;int:day&gt;/&lt;int:month&gt;/&lt;int:year&gt; 
    Have Fun! """

    html_message = "<html><body><pre>{}</pre></body></html>".format(message)
    return html_message


@app.route("/flights/<int:flight_id>", methods=["GET"])
def get_flight_by_id(flight_id):
    flight = flight_data.get_flight_by_id(flight_id)
    return jsonify(flight)


@app.route("/flights/delayed/<string:airline_name>", methods=["GET"])
def get_delayed_flights_by_airline(airline_name):
    delayed_flights = flight_data.get_delayed_flights_by_airline(airline_name)
    return jsonify(delayed_flights)


@app.route("/flights/delayed/airport/<string:airport_iata>", methods=["GET"])
def get_delayed_flights_by_airport(airport_iata):
    delayed_flights = flight_data.get_delayed_flights_by_airport(airport_iata)
    return jsonify(delayed_flights)


@app.route("/flights/<int:day>/<int:month>/<int:year>", methods=["GET"])
def get_flights_by_date(day, month, year):
    flights = flight_data.get_flights_by_date(day, month, year)
    return jsonify(flights)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
