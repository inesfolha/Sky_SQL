# Sky_SQL
<p id="top"></p>

## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
      - [File structure](#file-structure)
      - [API endpoints](#endpoints)
      - [Data Access Layer](#data-access-layer--dal-)
      - [Command-Line Interface](#command-line-interface--cli-)
      - [SQL Queries](#sql-queries)

3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Usage](#usage)
5. [Limitations](#limitations)
6. [Contribitions](#contributions)



## Introduction                                     
This project is a Flight Data API built with Flask and SQLAlchemy, allowing users to access and query flight data stored in a SQLite database. The API provides several endpoints to retrieve information about flights, including delayed flights, flights by airline, flights by airport, and flights by date.

[Back to the Top](#top)

## Description

### File Structure
Here's the file structure of the project:
```
.
├── .data
│   └── flights.sqlite3
├── app.py
├── data.py
├── main.py
├── sql_queries.py
└── README.md
```
[Back to the Top](#top)
### Endpoints

#### Home Endpoint

- URL: / 
- Method: GET 
- Description: Welcome message and available routes. 
- Example: http://localhost:5000/

#### Get Flight by ID

- URL: /flights/<int:flight_id>
- Method: GET 
- Description: Retrieve flight details by flight ID. 
- Example: http://localhost:5000/flights/123

#### Get Delayed Flights by Airline

- URL: /flights/delayed/<string:airline_name>
- Method: GET 
- Description: Retrieve delayed flights for a specific airline. 
- Example: http://localhost:5000/flights/delayed/Delta

#### Get Delayed Flights by Airport

- URL: /flights/delayed/airport/<string:airport_iata>
- Method: GET 
- Description: Retrieve delayed flights departing from a specific airport (by IATA code). 
- Example: http://localhost:5000/flights/delayed/airport/JFK

#### Get Flights by Date

- URL: /flights/<int:day>/<int:month>/<int:year>
- Method: GET 
- Description: Retrieve flights for a specific date. 
- Example: http://localhost:5000/flights/1/10/2023

[Back to the Top](#top)

### Data Access Layer (DAL)
The data.py module contains a Data Access Layer (DAL) class called FlightData, which interacts with the SQLite database. It provides methods for querying flight data based on various criteria, such as flight ID, airline name, airport code, and date.

### Command-Line Interface (CLI)
The main.py module serves as the command-line interface (CLI) for interacting with database. Users can select options from a menu to query flight data based on different parameters. 

The available options include:

- Show flight by ID 
- Show flights by date 
- Show delayed flights by airline 
- Show delayed flights by origin airport 
- Exit

[Back to the Top](#top)
### SQL Queries
The sql_queries.py module contains SQL queries used by the FlightData class to retrieve data from the SQLite database. These queries include retrieving flight details by ID, delayed flights by airline, delayed flights by airport, and flights by date.


[Back to the Top](#top)
## Installation

### Prerequisites

To run this project, you'll need Python 3 and the following dependencies:

- Flask
- SQLAlchemy

You can install these dependencies using pip:

``` python 
 pip install flask sqlalchemy
 ```

### Installation Steps

1. Clone this repository or download the script file:

```bash
git clone https://github.com/inesfolha/Sky_SQL.git
```

If you downloaded a ZIP archive, extract its contents to a directory of your choice.

2. Change to the script's directory:

 ```bash
  cd Sky_SQL
```
3. To run the script, open your terminal and execute the following command:
```bash
python main.py
```
Or to run the API open your terminal and execute the following command:
```bash
python app.py
```
This will start the Flask development server, and the API will be accessible at: http://localhost:5000

[Back to the Top](#top)

### Usage
 * [Watch Demo](link)


### Limitations
- Static Data: The flight data in the provided SQLite database (flights.sqlite3) is static and does not update in real-time. It represents a snapshot of data at a specific point in time.


- Performance: The API's query performance may vary based on query complexity and database size. Complex queries may take longer to execute, affecting response times.


- Security: This API does not include authentication or authorization mechanisms. It is intended for educational and non-production use. Security measures should be implemented when deploying in production.

## Contributions

Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and create a pull request.

[Back to the Top](#top)

