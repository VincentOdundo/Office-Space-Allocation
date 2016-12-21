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
        self.unallocated = []

    """ a method to handle room creation. it requires a room name as the input """
    def create_room(self, *args):
        try:
            for name in args:
                name, office_type = name.split('-')
                if name.lower() not in [room.room_name.lower() for room in self.rooms]:
                    """ check to see the type of room a person wishes to create """
                    if office_type == 'LivingSpace':
                        #create room of type LivingSpace if the type is LivingSpace
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

        #If person is a fellow and needs accomodation
        if person_type == 'Fellow' and self.accomodation == 'Y':
            person = Fellow(self.first_name, self.second_name)

            #increment the number of people in Amity
            self.people.append(person)
            #pick a random room and office from all the available office and livingspaces to assign the fellow
            if (self.accomodation == 'Y'):
                Vacant_living_spaces = self.check_vacant_rooms(self.livingspaces)
                Vacant_offices = self.check_vacant_rooms(self.offices)
                if(Vacant_living_spaces):
                      LivingSpace = random.choice(Vacant_living_spaces)
                      LivingSpace.current_occupancy.append(person)
                      person.alloted_living_space = LivingSpace.room_name
                else:
                    #add person to list of unallocated people
                    if person not in self.unallocated:
                        self.unallocated.append(person)
                if(Vacant_offices):
                    office = random.choice(Vacant_offices)
                    office.current_occupancy.append(person)
                    person.alloted_office = office.room_name
                else:
                    #add person to list of unallocated people
                    if person not in self.unallocated:
                        self.unallocated.append(person)
        elif person_type == 'Staff':
            person = Staff(self.first_name, self.second_name)
            #check for a vacant offices
            Vacant_offices = self.check_vacant_rooms(self.offices)
            #randomly pick one from the list of vacant offices
            if Vacant_offices:
                office = random.choice(Vacant_offices)
                #add the staff member to one of the offices and also to the list of persons
                person.alloted_office = office.room_name
                self.people.append(person)
                office.current_occupancy.append(person)
            else:
                #add person to list of unallocated people
                if person not in self.unallocated:
                    self.unallocated.append(person)
        else:
            person = Fellow(self.first_name, self.second_name)
            #check for a vacant offices
            Vacant_offices = self.check_vacant_rooms(self.offices)
            if Vacant_offices:
                office = random.choice(Vacant_offices)
                #add the staff member to one of the offices and also to the list of persons
                person.alloted_office = office.room_name
                self.people.append(person)
                office.current_occupancy.append(person)
            else:
                #add person to list of unallocated people
                if person not in self.unallocated:
                    self.unallocated.append(person)

    def check_vacant_rooms(self, list_of_rooms):
        """ A utility function to assist in picking up a vacant room"""
        vacant_rooms = []
        #process each room from the list of room objects to check it has space
        for room in list_of_rooms:
            if int(len(room.current_occupancy)) < room.no_of_occupants:
                vacant_rooms.append(room)
        #return the vacant rooms as a list
        return vacant_rooms

    #a utility function to return the room type
    def return_room_type(self, room_name):
        for room in self.rooms:
            if room.room_name == room_name:
                return room.room_type
            else:
                return False

    #a utility function to check a room exixts
    def check_room_exits(self, room_name):
        for room in self.rooms:
            if room.room_name == room_name:
                return room
            else:
                return False


    def reallocate_person(self, name, identifier, room_name):
        """ a method to implement the reallocations of persons in Amity """
        try:
            person = self.people[identifier]
            if person.person_type == 'Staff':
                #check for a vacant offices since staff can only assign an office
                Vacant_offices = self.check_vacant_rooms(self.offices)
                for room in Vacant_offices:
                    #check you are not reallocating a person to the same room again
                    if room.room_name == room_name and person not in room.current_occupancy:
                        room.current_occupancy.append(person)
                        #delete the person from the previous room alloted
                        for previous_room in self.offices:
                            if previous_room.room_name == person.alloted_office:
                                room.current_occupancy.remove(person)
                        person.alloted_office = room.room_name

                    else:
                        return "No Vacant offices or person already in the room or assigning a staff to a livingSpace!"

            elif person.person_type == 'Fellow':
                #to aid in picking the correct room type reallocation
                room_exists = self.check_room_exits(room_name)
                if room_exists:
                    room_reallocation_type = self.return_room_type(room_name)
                    if room_reallocation_type == 'livingSpace':
                        Vacant_rooms = self.check_vacant_rooms(self.livingspaces)
                    else:
                        Vacant_rooms = self.check_vacant_rooms(self.offices)
                    if Vacant_rooms and room_reallocation_type is not None:
                        for room in Vacant_rooms:
                            #check you are not reallocating a person to the same room again
                            if room.room_name == room_name and person not in room.current_occupancy:
                                room.current_occupancy.append(person)
                                #delete the person from the previous room alloted
                                for previous_room in self.rooms:
                                    if previous_room.room_name == person.alloted_office:
                                        previous_room.current_occupancy.remove(person)
                                        person.alloted_office = room.room_name
                                    elif previous_room.room_name == person.alloted_living_space:
                                        previous_room.current_occupancy.remove(person)
                                        person.alloted_living_space = room.room_name
                    else:
                        return "no Vacant rooms or person already in the room you are reallocating him/her!"
                else:
                    print('No room with such a name!')
        except IndexError:
            print('please check you are passing the correct person identifier!')

    #a method to implement Adds people to rooms from a txt file
    def load_people(self):
        filename = './people.txt'
        with open(filename, 'r') as persons_file:
            people = persons_file.readlines()
            if people:
                for Person in people:
                    person_details = Person.split()
                    person_firstname = person_details[0]
                    person_secondname = person_details[1]
                    person_type = person_details[2]
                    if person_type == 'FELLOW':
                        accomodation = person_details[3]
                        self.add_person(person_firstname, person_secondname, person_type, accomodation)
                    else:
                        accomodation = 'N'
                        self.add_person(person_firstname, person_secondname, person_type, accomodation)
            else:
                return "The text file is empty!"

    #Prints a list of allocations onto the screen
    def print_allocations(self):
        if self.rooms:
            allocations = ""
            for room in self.rooms:
                if room.current_occupancy:
                    allocations = room.room_name+"\n"
                    allocations += ", ".join([(person.first_name+' '+person.second_name+' '+person.person_type) for person in room.current_occupancy])
                    print (allocations)
                else:
                    allocations += "there are no people in {}".format(room.room_name)
                    print (allocations)
        else:
            print('there are no rooms in amity yet!')

    #Prints a list of unallocated people to the screen
    def print_unallocated(self):
        if self.unallocated:
            print('*****************************************************************')
            print('LIST OF UNALLOCATED PERSONS')
            print(", ".join([(person.first_name+' '+person.second_name+' '+person.person_type)
            for person in self.unallocated]))
        else:
            return "there are no unallocated persons!"
    #retrives a room with persons in the room given room name as input
    def print_room(self, room_name):
        retrieved_room = self.check_room_exits(room_name)
        if retrieved_room:
            print(retrieved_room.room_name)
            print('------------------------------------------------------------')
            print (", ".join([(person.first_name+' '+person.second_name+' '+person.person_type)
            for person in retrieved_room.current_occupancy]))
        else:
            return "No occupants in the room or room empty!"

    #Persists all the data stored in the app to a SQLite database
    @property
    def save_state(self):
        pass

    #Loads data from a database into the application
    @property
    def load_state(self):
        pass
amity = Amity()
amity.create_room('narnia-Office')
#amity.load_people()
amity.print_unallocated()
amity.print_allocations()
