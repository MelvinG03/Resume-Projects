""" Sort books by Library of Congress call number. """

from argparse import ArgumentParser
import re
import sys

class Book:
    """ A class for books with a call number from the Library of Congress
    
    Attributes:
        callnum (str): Call number of the book
        title (str): Title of the book
        author (str): Author of the book
    """
    def __init__(self, callnum, title, author):
        """ Set up the call number, title, and author of the book """
        self.callnum = callnum
        self.title = title
        self.author = author
    
    def __repr__(self):
        """ Returns a string of all the information """
        return f"Book({repr(self.callnum)}, {repr(self.title)}, {repr(self.author)})"
    
    def __lt__(self, other):
        """ Orders books by their call number """
        return self.parse_call_number(self.callnum) < self.parse_call_number(other.callnum)
    
    def parse_call_number(self, callnum):
        """ Parses the call number to be sorted """
        match = re.match(r'([A-Z]{1,3})(\d{1,4}(?:\.\d+)?)(?:\s*\.([A-Z]\d+))?(?:\s([A-Z]\d+))?\s*(\d{4})', callnum)
        if match:
            groups = match.groups()
            return (groups[0], float(groups[1]), groups[2] if groups[2] else '', groups[3] if groups[3] else '', int(groups[4]))
        return ()

def read_books(filename):
    """ Takes book information from the file and finds inidividual book lists and information """
    books = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            title, author, callnum = line.strip().split('\t')
            books.append(Book(callnum, title, author))
    return books

def print_books(books):
    """ Printing information about each book, in order. """
    for book in sorted(books):
        print(book)

def main(filename):
    """ Read book information from a file, sort the books by call number, and print information about each book. """
    books = read_books(filename)
    print_books(books)

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
