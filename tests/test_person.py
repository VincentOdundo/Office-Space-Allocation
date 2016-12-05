import unittest
from models.person import Person, Fellow
"""
Base class for all the tests regarding Person, Fellow and Staff Classes
"""

class TestClassPerson(unittest.TestCase):

    #create Objects from the classes person, Fellow, and Staff
    def setUp(self):
        self.person = Person('kayeli', 'dennis', 'Y')
        self.fellow = Fellow()

    # test to check if an object can be created from the class Person
    def testIsInstance(self):
        self.assertIsInstance(self.person, Person)

    #test to check an instance of the class person has all the attributes
    def test_person_attributes(self):
        self.assertTrue(hasattr(self.person, 'type'))
        self.assertTrue(hasattr(self.person, 'first_name'))
        self.assertTrue(hasattr(self.person, 'second_name'))

    #test to check an instance can be created from the class Fellow
    def testIsInstance(self):
        self.assertIsInstance(self.fellow, Fellow)

    #test for atttributes of a Fellow
    def test_fellow_attributes(self):
        self.assertTrue()
