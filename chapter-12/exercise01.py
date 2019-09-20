def find_dna_compliment(DNA: str) -> str:
    """Return a compliment of a DNA string
    >>> find_dna_compliment('AATTGCCGT')
    'TTAACGGCA'
    >>> find_dna_compliment('TTAACGGCA')
    'AATTGCCGT'
    """
    # start with an empty compliment DNA
    compliment = ''
    # take each character and append its opposite
    for char in DNA.upper():
        if char == 'A':
            compliment += 'T'
        if char == 'T':
            compliment += 'A'
        if char == 'G':
            compliment += 'C'
        if char == 'C':
            compliment += 'G'
    # return the compliment DNA
    return compliment

if __name__ == "__main__":
    import doctest
    doctest.testmod()