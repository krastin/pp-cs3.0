from atom import Atom

class Molecule:
    """A molecule with a name and a list of Atoms. """

    def __init__(self, name: str) -> None:
        """Create a Molecule named name with no Atoms.
        """
        self.name = name
        self.atoms = []

    def add(self, a: Atom) -> None:
        """Add a to my list of Atoms.
        """
        self.atoms.append(a)

    def __str__(self) -> str:
        """Return a string representation of this Molecule in this format:
        (NAME, (ATOM1, ATOM2, ...))
        """
        res = ''
        for atom in self.atoms:
            res = res + str(atom) + ', '
        # Strip off the last comma.
        res = res[:-2]
        return '({0}, ({1}))'.format(self.name, res)

    def __repr__(self) -> str:
        """Return a string representation of this Molecule in this format:
        Molecule("NAME", (ATOM1, ATOM2, ...))
        """
        res = ''
        for atom in self.atoms:
            res = res + repr(atom) + ', '
        # Strip off the last comma.
        res = res[:-2]
        return 'Molecule("{0}", ({1}))'.format(self.name, res)

    def translate(self, x: float, y: float, z: float) -> None:
        """Move this Molecule, including all Atoms, by (x, y, z).
        """
        for atom in self.atoms:
            atom.translate(x, y, z)