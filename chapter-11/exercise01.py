def find_dups(ints: list) -> set():
    '''takes a list of integers as its input argument and returns a set of those integers occurring two or more times in the list
    '''
    duplicates = []
    for element in ints:
        if ints.count(element) > 1:
            duplicates.append(element)
    return set(duplicates)

print(find_dups([1,2,3,1,4,1,5,2,6,7,3]))