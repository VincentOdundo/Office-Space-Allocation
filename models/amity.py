from models.room import Room, LivingSpace, Office
from models.person import Person, Fellow, Staff
import random

class Amity(object):
    name = 'Amity'
    def __init__(self):
        self.rooms = []
        self.people = []
        self.livingspaces = []
        self.offices = []

    """ a method to handle room creation. it requires a room name as the input """
    def create_room(self, *args):
        try:
            for name in args:
                name, office_type = name.split('-')
                if name.lower() not in [room.room_name.lower() for room in self.rooms]:
                    """ check to see the type of room a person wishes to create """
                    if office_type == 'LivingSpace':
                        """ create room of type LivingSpace if the type is LivingSpace """
                        room = LivingSpace(name)
                        self.rooms.append(room)
                        self.livingspaces.append(room)
                    else:
                        room = Office(name)
                        self.rooms.append(room)
                        self.offices.append(room)
                else:
                    return 'Sorry a room with the same name already exixts!'
        except NameError:
            return 'Sorry a room with the same name already exixts!'

    def add_person(self, first_name, second_name, person_type, accomodation=None):
        """ a method to implement adding a person to a room."""
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type
        self.accomodation = accomodation

        """ If person is a fellow and needs accomodation"""
        if person_type == 'Fellow':
            person = Fellow(self.first_name, self.second_name)

            #increment the number of people in Amity
            self.people.append(person)
            #pick a random room and office from all the available offices and livingspaces to assign the fellow
            if(self.accomodation == 'Y'):
                try:
                    if(self.livingspaces):
                        Vacant_living_spaces = self.check_vacant_rooms(self.livingspaces)
                        LivingSpace = random.choice(Vacant_living_spaces)
                        LivingSpace.current_occupancy.append(person)
                    else:
                        raise IndexError
                except IndexError:
                    return 'there are no vacant_rooms or there are no livingspaces!'
            try:
                if(self.offices):
                    Vacant_offices = self.check_vacant_rooms(self.offices)
                    office = random.choice(Vacant_offices)
                    office.current_occupancy.append(person)
                else:
                    raise IndexError
            except IndexError:
                return 'there are no offices or no vacant offices'
        elif person_type == 'Staff':
            person = Staff(self.first_name, self.second_name)
            #check for a vacant offices
            Vacant_offices = self.check_vacant_rooms(self.offices)
            #randomly pick one from the list of vacant offices
            office = random.choice(Vacant_offices)
            #add the staff member to one of the offices and also to the list of persons
            self.people.append(person)
            office.current_occupancy.append(person)
        else:
            person = Fellow(self.first_name, self.second_name)
            #check for a vacant offices
            Vacant_offices = self.check_vacant_rooms(self.offices)
            #randomly pick one from the list of vacant offices
            office = random.choice(Vacant_offices)
            self.people.append(person)
            office.current_occupancy.append(person)

    def check_vacant_rooms(self, list_of_rooms):
        """ A utility function to assist in picking up a vacant room"""
        vacant_rooms = []
        """ process each room from the list of room objects to check it has space"""
        for room in list_of_rooms:
            if int(len(room.current_occupancy)) < room.no_of_occupants:
                vacant_rooms.append(room)
        #return the vacant rooms as a list
        return vacant_rooms

    def reallocate_person(self, name, identifier, room_name):
        """ a method to implement the reallocations of persons in Amity """
        person = self.people[identifier]

        for room in self.rooms:
            if room.room_name == room_name:
                room.append(person)
                self.people.remove[person]


    #a method to implement Adds people to rooms from a txt file
    @property
    def load_people(self):
        pass

    #Prints a list of allocations onto the screen
    @property
    def print_allocations(self):
        pass

    #Prints a list of unallocated people to the screen
    @property
    def print_unallocated(self):
        pass

    def print_room(self, room_name):
        """ retrives a room with persons in the room given room name as input """
        pass

    #Persists all the data stored in the app to a SQLite database
    @property
    def save_state(self):
        pass

    #Loads data from a database into the application
    @property
    def load_state(self):
        pass
