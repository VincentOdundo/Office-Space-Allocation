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

    """ Test method for create_room in amity class"""
    def test_create_room(self):
        """ create a room of type office """
        room_one = self.Facility.create_room('narnia', 'O')

        """ check to see the rooms has been aded to the numer of rooms in amity"""
        self.assertEqual(len(self.Facility.rooms), 1)
        room_two = self.Facility.create_room('narnia', 'O')
        self.assertEqual(room_two, 'Sorry a room with the same name already exixts!')




        """ test to check a room name can only be characters"""
