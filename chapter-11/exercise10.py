from typing import Dict

def db_headings(dict_db: Dict) -> set:
    """takes a dictionary of dictionaries and
    returns the set of keys used in any of the inner dictionaries
    >>> dict_db = {'jgoodall' : {'surname' : 'Goodall', 'forename' : 'Jane', 'born' : 1934, 'died' : None, 'notes' : 'primate researcher', 'author' : [ 'In the Shadow of Man', 'The Chimpanzees of Gombe' ]}, 'rfranklin' : { 'surname' : 'Franklin', 'forename' : 'Rosalind', 'born' : 1920, 'died' : 1957, 'notes' : 'contributed to discovery of DNA'}, 'rcarson' : {'surname' : 'Carson', 'forename' : 'Rachel', 'born' : 1907, 'died' : 1964, 'notes' : 'raised awareness of effects of DDT', 'author' : [ 'Silent Spring' ] }}
    >>> output = db_headings(dict_db)
    >>> output.difference(set(['author', 'forename', 'surname', 'notes', 'born', 'died']))
    set()
    """
    headings = set()
    for person,data in dict_db.items():
        for k,v in data.items():
            headings.add(k)
    return headings

if __name__ == "__main__":
    import doctest
    doctest.testmod()