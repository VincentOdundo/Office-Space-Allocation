import unittest

from models.amity import Amity

"""
Base class for all the tests regarding Amity, and the Class Room
"""

class TestClassAmity(unittest.TestCase):
    def setUp(self):
        self.Facility = Amity()

    """ Test method for create_room in amity class"""
    def test_create_room(self):
        """ create a room of type office """
        room_one = self.Facility.create_room('narnia-Office')
        self.Facility.create_room('valahalla-Office')

        """ check to see the room has been added to the numer of rooms in amity"""
        self.assertEqual(len(self.Facility.rooms), 2)
        self.assertEqual(len(self.Facility.offices), 2)
        self.Facility.create_room('Hogwarts-LivingSpace')
        self.assertEqual(len(self.Facility.livingspaces), 1)

        """ Check to see you cannot add a room with the same name twice"""
        room_two = self.Facility.create_room('narnia-Office')
        self.assertEqual(room_two, 'Sorry a room with the same name already exixts!')

    def test_add_person(self):
        """ tests regarding adding a peson"""
        self.Facility.create_room('narnia-Office')
        self.Facility.create_room('Hogwarts-LivingSpace')
        """ add a person """
        self.Facility.add_person('kayeli', 'dennis', 'Fellow', 'Y')

        """ The list containnig the number of people should be extra one person"""
        self.assertEqual(len(self.Facility.people), 1)
        office = self.Facility.offices[0]
        livingSpace = self.Facility.livingspaces[0]
        self.assertEqual(len(office.current_occupancy), 1)
        self.assertEqual(len(livingSpace.current_occupancy), 1)

        """ add another fellow who doesnt need accomodation"""
        self.Facility.add_person('mary', 'muchai', 'Fellow', 'N')
        self.assertEqual(len(office.current_occupancy), 2)
        self.assertEqual(len(livingSpace.current_occupancy), 1)

    def test_reallocate_person(self):
        """ tests regarding printing people in a room"""
        self.Facility.create_room('narnia-Office')

        self.Facility.add_person('Dominic', 'Mogaka','Staff', 'N')
        self.Facility.add_person('Dennis', 'Mogaka','Staff', 'N')
        self.Facility.add_person('Felix', 'Mogaka','Fellow', 'Y')

        self.Facility.create_room('valahalla-Office')
        self.Facility.reallocate_person('Dennis', 0,'valahalla')
        self.assertEqual(len(self.Facility.offices[0].current_occupancy), 3)


    """ test whether the name attribute of class Amity can be modified """
    def test_amity_class_attributes_modification(self):
        setattr(self.Facility, self.Facility.name, 'Valhalla')
        self.assertNotEqual(self.Facility.name, 'Valhalla')
