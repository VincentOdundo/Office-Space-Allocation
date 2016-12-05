class Person(object):

    def __init__(self, first_name, second_name, type):
        self.first_name = first_name
        self.second_name = second_name
        if type is 'Y':
            self.type = Fellow()
        else:
            self.type = Staff()

class Fellow():
    pass

class Staff():
    pass
