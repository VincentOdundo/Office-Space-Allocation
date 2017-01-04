

class Person(object):
    """
    Class Person is the Base class for Person type Fellow and Staff
    """
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.person_identifier = id(self)



class Fellow(Person):
    """
    class Fellow inherits from the superclass person
    """
    def __init__(self, first_name, second_name):
        super(Fellow, self).__init__(first_name, second_name)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Fellow"
        self.alloted_office = None
        self.alloted_living_space = None
        self.person_identifier = id(self)

    def __str__():
        return self.person_type



class Staff(Person):
    """
    class Fellow inherits from the superclass person
    """
    def __init__(self, first_name, second_name):
        super(Staff, self).__init__(first_name, second_name)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Staff"
        self.alloted_office = None
        self.person_identifier = id(self)


    def __str__():
        return self.person_type
