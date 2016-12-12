
"""
Class Person is the Base class for Person type Fellow and Staff
"""
class Person(object):

    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

"""
class Fellow inherits from the superclass person
"""
class Fellow(Person):
    def __init__(self, first_name, second_name):
        super(Fellow, self).__init__(first_name, second_name)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Fellow"

    def __str__():
        return self.person_type


"""
class Fellow inherits from the superclass person
"""
class Staff(Person):
    def __init__(self, first_name, second_name):
        super(Staff, self).__init__(first_name, second_name)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Staff"

    def __str__():
        return self.person_type
