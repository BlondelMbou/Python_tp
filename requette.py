from flight_map import FlightMap 

# Création de l'objet FlightMap
fm = FlightMap()

# Chargement des aéroports depuis le fichier airports.csv
fm.import_airports('airports.csv')

# Chargement des vols depuis le fichier flights.csv
fm.import_flights('flights.csv')

# Accès à la liste des aéroports
print(fm.airport())

# Accès à la liste des vols
print(fm.flights())


print(str(fm.airport_find("FRA")))
