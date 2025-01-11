""" Build a database of energy sources in the US. """


from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    
    """ In-memory sqlite database for energy production data in the US by year and energy source

    Properties:
    conn (sqlite3.Connection): The connection to the sqlite database """
    
    def __init__(self, filename):
        
        """ Initialize the class. Connect to the sqlite database and also read data from the csv file

        Args:
        filename (str): Route to the csv file """

        self.conn = sqlite3.connect(':memory:')
        self.read(filename)
    
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass

    def read(self, filename):
        
        """ Reading the CSV and inputting data into the sqlite database

        Args:
        filename (str): Route to the csv file """

        cursor = self.conn.cursor()
        cursor.execute(""" CREATE TABLE production (year integer, state text, source text, mwh real)""")
        
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                year, state, source, mwh = line.strip().split(',')
                cursor.execute("INSERT INTO production VALUES (?, ?, ?, ?)", (int(year), state, source, float(mwh)))
        
        self.conn.commit()

    def production_by_source(self, source, year):
        
        """ Calculate the total energy produced about the year and the source

        Args:
        source (str): What energy source to use as a filter, ex. wind
        year (int): What year to use as a filter

        Returns:
        float: Total mega watt hours from the chosen energy source for the chosen year"""

        cursor = self.conn.cursor()
        cursor.execute("SELECT mwh FROM production WHERE source=? AND year=?", (source, year))
        results = cursor.fetchall()
        total_mwh = sum(row[0] for row in results)
        return total_mwh

def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
