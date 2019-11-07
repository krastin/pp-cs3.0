from members import Student, Faculty, Member

class Member(Member):
    """ Adding __repr__ to Member
    
    >>> joe = Member('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com')
    >>> joe
    Member('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com')
    >>> [joe]
    [Member('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com')]
    """
    def __repr__(self) -> str:
        return "Member('%s', '%s', '%s')" % (self.name, self.address, self.email)


class Faculty(Faculty):
    """ Adding __repr__ to Faculty
    
    >>> joe = Faculty('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 1234)
    >>> joe
    Faculty('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 1234)
    >>> [joe]
    [Faculty('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 1234)]
    """

    def __repr__(self) -> str:
        return "Faculty('%s', '%s', '%s', %d)" % (self.name, self.address, self.email, self.faculty_number)

class Student(Student):
    """ Adding __repr__ and __str__ to Student
    
    >>> joe = Student('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 4321)
    >>> joe
    Student('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 4321)
    >>> [joe]
    [Student('Joe Bonamassa', '1 Guitar Ave', 'joe@bona.com', 4321)]
    """

    def __repr__(self) -> str:
        return "Student('%s', '%s', '%s', %d)" % (self.name, self.address, self.email, self.student_number)

    def __str__(self) -> str:
        """
        >>> student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        >>> student.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nCourses: '
        """
        member_string = super().__str__()
        return '''{}\n{}\nCourses: {}'''.format(
        member_string,
        self.student_number,
        ' '.join(self.courses_taking))


if __name__ == "__main__":
    import doctest
    doctest.testmod()