class Nematode:
    """  a class called Nematode to keep track of information about C. elegans,
    including a variable for the body length (in millimeters; they are about
    1 mm in length), gender (either hermaphrodite or male), and age (in days).
    """

    def __init__(self, length: float, gender: str, age: int) -> None:
        self.length = length
        self.gender = gender
        self.age = age

    def __str__(self) -> str:
        return "A Nematode of %fmm, %s, %d days old)" % (self.length, self.gender, self.age)

    def __repr__(self) -> str:
        return "Nematode(%f, '%s', '%d')" % (self.length, self.gender, self.age)
