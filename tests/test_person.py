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


    """ test to check if an object can be created from the class Person """
    def testIsInstance(self):
        self.assertIsInstance(self.person, Person)
        self.assertIsInstance(self.fellow, Fellow)

    """ test to check an instance of the class person has all the attributes """
    def test_person_attributes(self):
        self.assertEqual(self.staff.person_type, 'Staff')
        self.assertTrue(hasattr(self.staff, 'first_name'))
        self.assertTrue(hasattr(self.staff, 'second_name'))

    """ test for atttributes of a Fellow """
    def test_fellow_attributes(self):
        self.assertEqual(self.fellow.person_type, 'Fellow')
        self.assertTrue(hasattr(self.fellow, 'first_name'))
        self.assertTrue(hasattr(self.fellow, 'second_name'))
