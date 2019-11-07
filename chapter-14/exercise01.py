class Country:
    """ A Country with name, population and area
    >>> canada = Country('Canada', 34482779, 9984670)
    >>> canada.name
    'Canada'
    >>> canada.population
    34482779
    >>> canada.area
    9984670
    >>> usa = Country('United States of America', 313914040, 9826675)
    >>> print(usa)
    United States of America has a population of 313914040 and is 9826675 square km.
    >>> canada.is_larger(usa)
    True
    >>> canada.population_density()
    3.4535722262227995
    >>> canada
    Country('Canada', 34482779, 9984670)
    >>> [canada]
    [Country('Canada', 34482779, 9984670)]
    """

    def __init__(self, name: str, population: int, area: int) -> None:
        """ Create a Country """
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self) -> str:
        return "Country('%s', %d, %d)" % (self.name, self.population, self.area)

    def __str__(self) -> str:
        return "%s has a population of %d and is %d square km." % (self.name, self.population, self.area)

    def is_larger(self, country) -> bool:
        return self.area > country.area

    def population_density(self) -> float:
        return self.population / float(self.area)

if __name__ == "__main__":
    import doctest
    doctest.testmod()