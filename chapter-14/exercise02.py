from exercise01 import Country

from typing import List

class Continent:
    """ A continent that has one or more countries
    >>> canada = Country('Canada', 34482779, 9984670)
    >>> usa = Country('United States of America', 313914040, 9826675)
    >>> mexico = Country('Mexico', 112336538, 1943950)
    >>> countries = [canada, usa, mexico]
    >>> north_america = Continent('North America', countries)
    >>> north_america.name
    'North America'
    >>> for country in north_america.countries:
    ...   print(country)
    ... 
    Canada has a population of 34482779 and is 9984670 square km.
    United States of America has a population of 313914040 and is 9826675 square km.
    Mexico has a population of 112336538 and is 1943950 square km.
    >>> north_america.total_population()
    460733357
    >>> print(north_america)
    North America
    Canada has a population of 34482779 and is 9984670 square km.
    United States of America has a population of 313914040 and is 9826675 square km.
    Mexico has a population of 112336538 and is 1943950 square km.
    """

    def __init__(self, name: str, countries: List[Country]) -> None:
        self.name = name
        self.countries = countries
    
    def __str__(self) -> str:
        output = self.name
        for country in self.countries:
            output += "\n%s" % country
        return output

    def total_population(self) -> int:
        total = 0
        for country in self.countries:
            total += country.population
        return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()