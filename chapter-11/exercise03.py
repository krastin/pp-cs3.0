from typing import Set

def mating_pairs(males: Set, females: Set) -> Set:
    '''takes two equal-sized sets called males and females as input and
    returns a set of pairs; each pair must be a tuple containing one male and one
    female. (The elements of males and females may be strings containing gerbil
    names or gerbil ID numbers - works with both
    >>> males = set(["Tom"])
    >>> females = set(["Tamara"])
    >>> result = mating_pairs(males, females)
    >>> result
    {('Tom','Tamara')}
    '''
    if len(males) != len(females):
        print('Sets have different length')
        return None
    output = []
    while len(males) > 0:
        output.append((males.pop(), females.pop()))
    return set(output)


males = set(["Tom", "Vance", "Jose", "Tyler", "Nathan"])
females = set(["Tamara", "Margaret", "Mae", "Perla", "Emmie"])

print(mating_pairs(males, females))