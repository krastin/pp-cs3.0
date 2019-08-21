from typing import Set

def read_authors(*filenames):
    """takes a list of filenames as an input argument and returns the set of all author
    names found in those files.
    >>> instring = 'AUTHOR Jimbob\tTheBatman   Cowalski\\nCOMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_authors(infile)
    {'Jimbob TheBatman Cowalski'}
    """
    authors = []
    for filename in filenames:
        try:
            with open(filename, 'r') as input_file:
                line = True
                while line is not '':
                    line = input_file.readline()
                    if line[:6].upper() == 'AUTHOR':
                        authors.append(line[6:].strip())
                    else:
                        continue
        except:
            print('Failed opening file ', filename)
    return set(authors)

print(read_authors('multimol.pdb'))