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
