import unittest
from models.person import Person, Fellow, Staff
"""
Base class for all the tests regarding Person, Fellow and Staff Classes
"""

class TestClassPerson(unittest.TestCase):

    """ create Objects from the classes person, Fellow, and Staff """
    def setUp(self):
        #instantiate objects from the model classes regarding a person entity
        self.person = Person('kayeli', 'dennis')
        self.fellow = Fellow('kayeli', 'dennis')
        self.staff = Staff('kayeli', 'dennis')

    """ test to check both class Fellow and Staff are subclass to class Person"""
    def test_fellow_staff_subclass(self):
        self.assertTrue(issubclass(Fellow, Person))
        self.assertTrue(issubclass(Staff,Person))
