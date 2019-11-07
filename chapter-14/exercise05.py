from math import sqrt

class Point:
    """ A Point in (x,y) coordinates
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class LineSegment:
    """ A line segment
    >>> segment = LineSegment(Point(1, 1), Point(3, 2))
    >>> segment.slope()
    0.5
    >>> segment.length()
    2.23606797749979
    """

    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2
        
    def slope(self) -> float:
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def length(self) -> float:
        return sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()