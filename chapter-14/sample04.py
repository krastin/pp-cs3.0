from members import Student, Faculty

paul = Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')
print(paul.name)

print(paul.email)

print(paul.faculty_number)

print(paul)


jen = Student('Jen Campbell', 'Toronto', 'campbell@cs.toronto.edu', '4321')
print(jen.name)

print(jen.email)

print(jen.student_number)

print(jen)