class UniqueWords:
    
    """ A class to track unique words across multiple text files

    Attributes:
        all_words (set): A set containing all words encountered in the files read.
        unique_words (set): A set containing words that appear in only one file.
        words_by_file (dict): A dictionary mapping filenames (keys) to sets of words (values) that appear in each file. """

    def __init__(self):
        
        """ Initializing the UniqueWords class. Create two empty sets and one dictionary set """
        
        self.all_words = set()
        self.unique_words = set()
        self.words_by_file = {}

    def add_file(self, filename, key):
        
        """ Adding a file with three parameters, self, filename, and key

        Args:
            filename (string): The path for how the code is going to read the file
            key (string): The nickname for the file """
        
        with open(filename, 'r') as file:
            reading = file.read()
        
        words = get_words(reading)
        words_set = set(words)
        
        self.words_by_file[key] = words_set
        self.unique_words.difference_update(words_set)
        new_unique_words = words_set.difference(self.all_words)
        self.unique_words.update(new_unique_words)
        self.all_words.update(words_set)
    
    def unique(self, key):
        
        """ Taking the unique words from the specific file

        Args:
            key (string): The nickname for the file

        Result:
            set: The set of words from the specific file """
        
        if key not in self.words_by_file:
            raise ValueError(f"There is no file with '{key}'")
        
        file_words = self.words_by_file[key]
        
        unique_to_file = set()
        for word in file_words:
            if word in self.unique_words:
                unique_to_file.add(word)
        
        return unique_to_file

def get_words(s):

    """ Extract a list of words from string s

    Args:
        s (str): a string containing one or more words

    Returns:
        list of str: a list of words from s converted to lower-case """
    
    import re
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words

