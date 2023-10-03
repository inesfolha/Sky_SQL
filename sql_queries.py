QUERY_FLIGHT_BY_ID = """
SELECT f.*, a.airline, f.ID as FLIGHT_ID, f.DEPARTURE_DELAY as DELAY 
FROM flights AS f
JOIN airlines AS a 
  ON f.airline = a.id WHERE f.ID = :id
  """

QUERY_DELAYED_FLIGHTS_BY_AIRLINE = """
SELECT f.*, a.airline, f.ID as FLIGHT_ID, f.DEPARTURE_DELAY as DELAY 
FROM flights AS f
JOIN airlines AS a 
  ON f.airline = a.id 
WHERE a.airline = :airline_name AND f.DEPARTURE_DELAY > 20
"""

QUERY_DELAYED_FLIGHTS_BY_AIRPORT = """
SELECT f.*, a.airline, f.ID as FLIGHT_ID, f.DEPARTURE_DELAY as DELAY 
FROM flights AS f 
JOIN airlines AS a
  ON f.airline = a.id 
WHERE f.ORIGIN_AIRPORT = :airport_iata AND f.DEPARTURE_DELAY > 20
"""

QUERY_FLIGHTS_BY_DATE = """
SELECT f.*, a.airline, f.ID as FLIGHT_ID, f.DEPARTURE_DELAY as DELAY 
FROM flights AS f
JOIN airlines AS a 
  ON f.airline = a.id 
WHERE f.DAY = :day AND f.MONTH = :month AND f.YEAR = :year
"""