from io import StringIO
from typing import TextIO

def hopedale_average(reader: TextIO) -> int:
    '''a. Write an outline in English of the algorithm you would use to read
    the values from this data set to compute the average number of pelts
    produced per year.
    b. Translate your algorithm into Python by writing a function named
    hopedale_average that takes a filename as a parameter and returns the
    average number of pelts produced per year.
    >>> with open('hopedale.txt', 'r') as input_file:
    ...    hopedale_average(input_file)
    41.44444444444444
    '''
    years = 0
    pelts = 0
    # Read the description line
    line = reader.readline()
    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first real piece of data
    pelts += int(line)
    years += 1
    for line in reader:
    	pelts += int(line)
    	years += 1
    return float(pelts/years)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
