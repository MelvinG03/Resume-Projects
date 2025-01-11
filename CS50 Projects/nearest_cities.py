from argparse import ArgumentParser
import sys
from haversine import haversine

class Cities:
    def __init__(self, filename):
        
        """ Create the Cities class and take in city data from files

        Args:
        filename (string): Getting the city data. 4 values: State/country, city, latitude, and longitude """

        self.cities = {}
        with open(filename, 'r') as file:
            for line in file:
                area, city, lat, lon = line.strip().split(',')
                self.cities[(area, city)] = (float(lat), float(lon))

    def nearest(self, point):
        """
        To five the closest 5 cities from the chosen point on the coordinate map

        Args:
        point (tuple): Holding latitude and longitude as floats

        Returns:
        list: Listing out the five closest cities to the coordinate """

        sorted_cities = sorted(self.cities.keys(), key=lambda x: haversine(point, self.cities[x]))
        return sorted_cities[:5]

def main(filename, arg1, arg2):
    """
    Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).

    Args:
    filename (str): Path to a file containing city data. Each line
                    in the file should consist of four values, separated by
                    commas: area (e.g., state or country), city, latitude in
                    decimal degrees, longitude in decimal degrees.
    arg1 (str): Either the name of an area in the file, or a string
                representation of a latitude.
    arg2 (str): Either the name of a city in the file, or a string
                representation of a longitude.

    Side effects:
    Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[(arg1, arg2)]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")

    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print(" " + ", ".join(result))

def parse_args(arglist):
    """
    Process command-line arguments and return the parsed values as a namespace.

    Args:
    arglist (list): List of command-line arguments.

    Returns:
    Namespace: Parsed command-line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1",
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)  
