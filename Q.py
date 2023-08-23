class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = [flight for flight in self.flights if city in (flight.source, flight.destination)]
        return result

    def search_by_source(self, source):
        result = [flight for flight in self.flights if flight.source == source]
        return result

    def search_between_cities(self, source, destination):
        result = [flight for flight in self.flights if flight.source == source and flight.destination == destination]
        return result

def main():
    flight_table = FlightTable()

    # Populate flight table
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    city_mapping = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city code (e.g., BLR): ")
        city_name = city_mapping.get(city, "Unknown")
        results = flight_table.search_by_city(city)
        print(f"Flights related to {city_name}:")
        for flight in results:
            print(f"Flight ID: {flight.flight_id}, From: {city_mapping[flight.source]}, To: {city_mapping[flight.destination]}, Price: {flight.price}")
    elif choice == 2:
        source = input("Enter the source city code (e.g., BLR): ")
        source_name = city_mapping.get(source, "Unknown")
        results = flight_table.search_by_source(source)
        print(f"Flights from {source_name}:")
        for flight in results:
            print(f"Flight ID: {flight.flight_id}, To: {city_mapping[flight.destination]}, Price: {flight.price}")
    elif choice == 3:
        source = input("Enter the source city code (e.g., BLR): ")
        destination = input("Enter the destination city code (e.g., BOM): ")
        source_name = city_mapping.get(source, "Unknown")
        destination_name = city_mapping.get(destination, "Unknown")
        results = flight_table.search_between_cities(source, destination)
        print(f"Flights from {source_name} to {destination_name}:")
        for flight in results:
            print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
