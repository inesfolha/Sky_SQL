from sqlalchemy import create_engine, text
from sql_queries import (
    QUERY_FLIGHT_BY_ID,
    QUERY_DELAYED_FLIGHTS_BY_AIRLINE,
    QUERY_DELAYED_FLIGHTS_BY_AIRPORT,
    QUERY_FLIGHTS_BY_DATE,
)

class FlightData:
    """
    The FlightData class is a Data Access Layer (DAL) object that provides an
    interface to the flight data in the SQLITE database. When the object is created,
    the class forms connection to the sqlite database file, which remains active
    until the object is destroyed.
    """
    def __init__(self, db_uri):
        """
        Initialize a new engine using the given database URI
        """
        self._engine = create_engine(db_uri)

    def _execute_query(self, query, params):
      """
      Execute an SQL query with the params provided in a dictionary,
      and returns a list of records (dictionary-like objects).
      If an exception was raised, print the error, and return an empty list.
      """
      try:
          # Create a connection and execute the query with the provided params
          with self._engine.connect() as connection:
              result = connection.execute(text(query), **params)

          # get all rows and convert them into a list of dictionary-like records
              records = [dict(row) for row in result]
          return records

      except Exception as error:
        # Catch any other unexpected exceptions
          print("Error executing query:", error)
          return []

    def get_flight_by_id(self, flight_id):
        """
        Searches for flight details using flight ID.
        If the flight was found, returns a list with a single record.
        """
        params = {'id': flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)

    def get_delayed_flights_by_airline(self, airline_name):
        """
        Searches for delayed flights for a given airline.
        Returns a list of dictionary-like objects with flight details.
        """
        params = {'airline_name': airline_name}
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRLINE, params)

    def get_delayed_flights_by_airport(self, airport_iata):
        """
        Searches for delayed flights for a given airport (by IATA code).
        Returns a list of dictionary-like objects with flight details.
        """
        params = {'airport_iata': airport_iata}
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRPORT, params)

    def get_flights_by_date(self, day, month, year):
        """
        Searches for flights for a given date.
        Returns a list of dictionary-like objects with flight details.
        """
        params = {'day': day, 'month': month, 'year': year}
        return self._execute_query(QUERY_FLIGHTS_BY_DATE, params)


    def __del__(self):
        """
        Closes the connection to the databse when the object is about to be destroyed
        """
        self._engine.dispose()
    