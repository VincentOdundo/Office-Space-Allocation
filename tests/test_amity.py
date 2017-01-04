import unittest

from models.amity import Amity

class TestClassAmity(unittest.TestCase):
    """
    Base class for all the tests regarding Amity, and the Class Room
    """
    def setUp(self):
        self.Facility = Amity()

    def test_create_room(self):
        """ Test method for create_room in amity class"""
        previous_room_count = len(self.Facility.rooms)
        #create a room of type office
        self.Facility.create_room('Office', 'narnia')
        self.Facility.create_room('Office', 'valahalla')
        #check the number of rooms has incremented
        self.assertNotEqual(len(self.Facility.rooms), previous_room_count)
        #Check to see you cannot add a room with the same name twice
        room_two = self.Facility.create_room('Office', 'narnia')
        self.assertEqual(room_two, 'narnia room exists or you cannot create a room with the same name twice!')

    def test_add_person(self):
        """ tests regarding adding a peson """
        previous_count = len(self.Facility.people)
        #add a person
        self.Facility.add_person('kayeli', 'dennis', 'Fellow', 'Y')
        #assert people count has increased
        self.assertNotEqual(len(self.Facility.people), previous_count)

        previous_unallocated_count = self.Facility.unallocated
        #assert the number of people in unallocated list has incremented
        self.assertNotEqual(len(self.Facility.unallocated), previous_unallocated_count)

    def test_reallocate_person(self):
        """ tests regarding reallocating a person to a different room"""
        self.Facility.create_room('Office', 'narnia')
        self.Facility.add_person('Dominic', 'Mogaka','Staff', 'N')
        person_count_in_nania = self.Facility.rooms[0].current_occupancy
        new_person = self.Facility.people[0]

        self.Facility.create_room('Office', 'valahalla')
        self.Facility.reallocate_person(new_person.person_identifier, 'valahalla')
        self.assertNotEqual(len(self.Facility.rooms[0].current_occupancy), person_count_in_nania)
