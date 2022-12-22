import csv
from airports import Airport
from flight import Flight

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
    
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader: 
                print(row)
            # self.airports = [Airport(*row) for row in reader]

           
    
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader: 
                print(row)
            # self.flights = [Flight(*row) for row in reader]
    
    def airports(self) -> list[Airport]:
        return self.airports
    
    def flights(self) -> list[Flight]:
        return self.flights
    
    def airport_find(self, airport_code: str) -> Airport:
        for airport in self.airports:
            if airport.code == airport_code:
                return airport
        return None
    
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for flight in self.flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
        return False
    
    def flights_where(self, airport_code: str) -> list[Flight]:
        return [flight for flight in self.flights if flight.src_code == airport_code or flight.dst_code == airport_code]
    
    def airports_from(self, airport_code: str) -> list[Airport]:
        flights = self.flights_where(airport_code)
        airport_codes = {flight.dst_code for flight in flights}
        return [self.airport_find(code) for code in airport_codes]


