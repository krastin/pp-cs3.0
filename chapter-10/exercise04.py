from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
        """Skip the header in reader and return the first real piece of data.
        >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
        >>> skip_header(infile)
        'Data line\\n'
        """
        # Read the description line
        line = reader.readline()
        # Find the first non-comment line
        line = reader.readline()
        while line.startswith('#'):
                line = reader.readline()
        # Now line contains the first real piece of data
        return line

def find_largest(line: str) -> int:
    """Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.
    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """
    # The largest value seen so far.
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v
    return largest

def process_file(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header. There may be multiple pieces
    of data on each line.
    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """
    line = skip_header(reader).strip()
    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)
    # Check the rest of the lines for larger values.
    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large
    return largest