from flightMap import FlightMap 

fm = FlightMap()
fm.import_airports('airports.csv')
fm.import_flights('flights.csv')

# affiche la liste des aéroports
print(fm.airports())

# affiche la liste des vols
print(fm.flights())
