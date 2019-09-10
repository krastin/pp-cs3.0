from typing import TextIO, Tuple, Dict
from io import StringIO

Atom = Tuple[str, Tuple[str, str, str]]
CompoundDict = Dict[str, Atom]

def read_molecule(reader: TextIO) -> CompoundDict:
    """Read a single molecule from reader and return it, or return None to
    signal end of file. The returned dictionary has one key/value pair where
    the key is the name of the compound and the value is a list of Atoms.
    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    {'TEST': [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]}
    """
    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None
    
    while line.strip() is '':
        line = reader.readline()
        if not line:
            return None
    
    # Name of the molecule: "COMPND name"
    parts = line.split()
    name = parts[1]
    
    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule_list = []
    reading = True
    while reading:
        molecule = []
        line = reader.readline()
        if line.startswith('END'):
            reading = False
            continue
        if line.startswith('CMNT'):
            continue
        else:
            parts = line.split()
            element = parts[2]
            numbers = tuple(parts[3:])
            molecule = tuple([element, numbers])
            molecule_list.append(molecule)
    return {name : molecule_list}

def read_all_molecules(reader: TextIO) -> CompoundDict:
    """Read zero or more molecules from reader, returning a list of the
    molecule information.
    >>> cmpnd1 = 'COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> cmpnd2 = 'COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result['T1']
    [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]
    >>> result['T2']
    [('A', ('0.1', '0.2', '0.3')), ('A', ('0.2', '0.1', '0.0'))]
    """
    # The list of molecule information.
    result = {}
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: # None is treated as False in an if statement
            result = {**result, **molecule}
        else:
            reading = False
    return result

if __name__ == '__main__':
    with open('multimol.pdb', 'r') as input_file:
        output = read_all_molecules(input_file)
    print(output)