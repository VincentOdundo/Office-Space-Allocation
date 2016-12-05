import unittest

from models.amity import Amity

"""
Base class for all the tests regarding Amity, and the Class Room
"""

class TestClassAmity(unittest.TestCase):
    def setUp(self):
        self.Facility = Amity()

    """ test to check if an object can be created from the class Amity """
    def testIsInstance(self):
        self.assertIsInstance(self.Facility, Amity)

    """ test object has Amity class variables """
    def test_amity_class_variables(self):
        self.assertEqual(self.Facility.name, 'Amity')

    """ test whether the name attribute of class Amity can be modified """
    def test_amity_class_attributes_modification(self):
        setattr(self.Facility, self.Facility.name, 'Valhalla')
        self.assertNotEqual(self.Facility.name, 'Valhalla')

    """ test to attest class Amity has all the methods """
    def test_amity_properties(self):
        self.assertTrue(hasattr(self.Facility, 'create_room'))
        self.assertTrue(hasattr(self.Facility, 'add_person'))
        self.assertTrue(hasattr(self.Facility, 'reallocate_person'))
        self.assertTrue(hasattr(self.Facility, 'load_people'))
        self.assertTrue(hasattr(self.Facility, 'print_allocations'))
        self.assertTrue(hasattr(self.Facility, 'print_unallocated'))
        self.assertTrue(hasattr(self.Facility, 'print_room'))
        self.assertTrue(hasattr(self.Facility, 'save_state'))
        self.assertTrue(hasattr(self.Facility, 'load_state'))
