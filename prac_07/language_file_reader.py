"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year,PointerArithmetic
        in_file.readline()
        # All other lines are language data
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split(',')
            # Reflection and Pointer Arithmetic are stored as strings (Yes/No) and we want Booleans
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            # Construct a ProgrammingLanguage object using the elements
            # year should be an int
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            # Add the language we've just constructed to the list
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)
        # Language will be a new subclass of the tuple data type class
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)  # use default dialect, Excel

        for row in reader:
            # Convert reflection and pointer_arithmetic to Booleans
            row[2] = row[2] == "Yes"
            row[4] = row[4] == "Yes"
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("languages.csv", "r") as in_file:
        in_file.readline()
        for language in map(Language._make, csv.reader(in_file)):
            # Convert reflection and pointer_arithmetic to Booleans
            language = language._replace(reflection=language.reflection == "Yes",
                                         pointer_arithmetic=language.pointer_arithmetic == "Yes")
            print(language.name, 'was released in', language.year)
            print(repr(language))


if __name__ == '__main__':
    main()
