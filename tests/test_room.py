import unittest
from models.room import Room, LivingSpace, Office

class TestClassRoom(unittest.TestCase):
    """ instantiate objects from the the Room class"""
    def setUp(self):
        self.room = Room('Narnia')
        self.livingSpace = LivingSpace('chania')
        self.office = Office('oculus')

    """ test to check if an object can be created from the class Room """
    def testIsInstance(self):
        self.assertIsInstance(self.room, Room)
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.livingSpace, LivingSpace)

    """ test to expose the properites of the instances of livingSpace and Office"""
    def test_propertiies_office_livingspace(self):
        self.assertTrue(hasattr(self.livingSpace, 'no_of_occupants'))
        self.assertTrue(hasattr(self.office, 'no_of_occupants'))

        #get number of occupants from the wo instaces of office and livingSpace respectively
        number_of_occupants_office = self.office.no_of_occupants
        number_of_occupants_living = self.livingSpace.no_of_occupants

        #assert they pick the correct values allocated as its number of occupants
        self.assertEqual(number_of_occupants_office, 6)
        self.assertEqual(number_of_occupants_living, 4)
