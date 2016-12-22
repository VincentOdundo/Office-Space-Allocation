from models.room import Room, LivingSpace, Office
from models.person import Person, Fellow, Staff
from models.database import AmityOffices, AmityLiving, Persons, create_db, Base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
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
    def create_room(self, office_type, args):
        for room in args:
            if room.lower() not in [room.room_name.lower() for room in self.rooms]:
                if office_type.lower() == 'livingspace':
                    room = LivingSpace(room)
                    self.rooms.append(room)
                    self.livingspaces.append(room)
                else:
                    room = Office(room)
                    self.rooms.append(room)
                    self.offices.append(room)
            else:
                print('{} room exixts or you cannot create a room with the same name twice!'.format(room))

    def add_person(self, first_name, second_name, person_type, accomodation=None):
        """ a method to implement adding a person to a room."""
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type
        self.accomodation = accomodation

        message = "Person added to the system!"
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
                      message += "Fellow successfully assigned a room!"
                else:
                    #add person to list of unallocated people
                    if person not in self.unallocated:
                        self.unallocated.append(person)
                    message +="No living spaces alloted!"
                if(Vacant_offices):
                    office = random.choice(Vacant_offices)
                    office.current_occupancy.append(person)
                    person.alloted_office = office.room_name
                    message += "Fellow successfully assigned an Office!"
                else:
                    #add person to list of unallocated people
                    if person not in self.unallocated:
                        self.unallocated.append(person)
                    message += "No Office alloted!"

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
                message += "Staff Member successfully assigned an Office!"
            else:
                #add person to list of unallocated people
                if person not in self.unallocated:
                    self.unallocated.append(person)
                message += "No Office alloted!"
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
                message += "Fellow successfully assigned an Office!"
            else:
                #add person to list of unallocated people
                if person not in self.unallocated:
                    self.unallocated.append(person)
                message += "No Office alloted!"
        message += "Person Identifier:"+str(person.person_identifier)
        print(message)

    def check_vacant_rooms(self, list_of_rooms):
        """ A utility function to assist in picking up a vacant room"""
        vacant_rooms = []
        #process each room from the list of room objects to check it has space
        for room in list_of_rooms:
            if int(len(room.current_occupancy)) < room.no_of_occupants:
                vacant_rooms.append(room)
        #return the vacant rooms as a list
        return vacant_rooms

    #a utility function to check a room exixts
    def check_room_exits(self, room_name):
        for room in self.rooms:
            if room.room_name == room_name:
                return room
            else:
                return False

    def reallocate_person(self, identifier, room_name):
        """ a method to implement the reallocations of persons in Amity """
        found_person = None
        for person in self.people:
            if person.person_identifier == int(identifier):
                found_person = person
        if found_person is not None:
            message = 'No Vacant offices or person already in the room or assigning a staff to a livingSpace!'
            if found_person.person_type == 'Staff':
                #check for a vacant offices since staff can only assign an office
                print(self.offices)
                Vacant_offices = self.check_vacant_rooms(self.offices)
                for room in Vacant_offices:
                    #check you are not reallocating a person to the same room again
                    if room.room_name == room_name and found_person not in room.current_occupancy:
                        room.current_occupancy.append(found_person)
                        #delete the person from the previous room alloted
                        message = 'reallocation success!'
                        for previous_room in self.offices:
                            if previous_room.room_name == found_person.alloted_office:
                                room.current_occupancy.remove(found_person)
                                found_person.alloted_office = room.room_name
                print(message)
            elif found_person.person_type == 'Fellow':
                #to aid in picking the correct room type reallocation
                found_room = None
                found_office_type = None
                for room in self.rooms:
                    if room.room_name == room_name:
                        found_room = room
                if found_room:
                    if found_room.room_type.lower() == 'livingSpace':
                        Vacant_rooms = self.check_vacant_rooms(self.livingspaces)
                        found_room_type = 'livingSpace'
                    else:
                        Vacant_rooms = self.check_vacant_rooms(self.offices)
                        found_room_type = 'Office'
                if Vacant_rooms:
                    success_message = ''
                    for room in Vacant_rooms:
                    #check you are not reallocating a person to the same room again
                        if room.room_name == room_name and found_person not in room.current_occupancy:
                            room.current_occupancy.append(found_person)
                            #delete the person from the previous room alloted
                            for previous_room in self.rooms:
                                if previous_room.room_name == found_person.alloted_office:
                                    previous_room.current_occupancy.remove(found_person)
                                    found_person.alloted_office = room.room_name
                                elif previous_room.room_name == found_person.alloted_living_space:
                                    previous_room.current_occupancy.remove(found_person)
                                    found_person.alloted_living_space = room.room_name
                        success_message = 'reallocation success!'
                    print(success_message)
        else:
            print('Person Not Found!')

    #a method to implement Adds people to rooms from a txt file
    def load_people(self, filename):
        try:
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
        except IOError:
            print('File name not in directory or you are passing wrong file type!')


    #Prints a list of allocations onto the screen
    def print_allocations(self, args):
        allocations = ""
        if self.rooms:
            for room in self.rooms:
                if room.current_occupancy:
                    allocations = room.room_name+"\n"
                    allocations += ", ".join([(person.first_name+' '+person.second_name+' '+person.person_type) for person in room.current_occupancy])
                    print (allocations)
                else:
                    allocations += "there are no people in {}".format(room.room_name)
        else:
            allocations = 'there are no rooms in amity yet!'
        if args:
            with open(args, 'wt') as filename:
                filename.write(allocations)
        else:
            print (allocations)

    #Prints a list of unallocated people to the screen
    def print_unallocated(self, args):
        output = ""
        if self.unallocated:
            output += '*****************************************************************\n'
            output += 'LIST OF UNALLOCATED PERSONS'
            output += ", ".join([(person.first_name+' '+person.second_name+' '+person.person_type)
            for person in self.unallocated])
        else:
            output += "there are no unallocated persons!"
        #output to a file
        if args:
            with open(args, 'wt') as filename:
                filename.write(output)
        else:
            print (output)

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
    def save_state(self, dbname='Amity'):
        engine = create_db(dbname)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        #retrieve offices from the Database
        offices_from_db = select([AmityOffices])
        result = session.execute(offices_from_db)
        room_names_from_db = [row.room_name for row in result]
        for room in self.offices:
            if room.room_name not in room_names_from_db:
                new_room = AmityOffices(room_name=room.room_name)
                session.add(new_room)
                session.commit()
        #retrieve livingspaces from the Database
        livingspaces_from_db = select([AmityLiving])
        result = session.execute(livingspaces_from_db)
        livingspaces_names_from_db = [row.room_name for row in result]
        for room in self.livingspaces:
            if room.room_name not in livingspaces_names_from_db:
                new_room = AmityLiving(room_name=room.room_name)
                session.add(new_room)
                session.commit()

        #retrieve People from the Database
        persons_from_db = select([Persons])
        result = session.execute(persons_from_db)
        person_identifier_from_db = [row.person_identifier for row in result]
        for person in self.people:
            if person.person_identifier not in person_identifier_from_db:
                if person.person_type == 'Staff':
                    new_person = Persons(fname=person.first_name, lname=person.second_name, person_identifier=person.person_identifier, role=person.person_type, office_allocated=person.alloted_office)
                else:
                    new_person = Persons(fname=person.first_name, lname=person.second_name, person_identifier=person.person_identifier, role=person.person_type, office_allocated=person.alloted_office, living_allocated=person.alloted_living_space)
                session.add(new_person)
                session.commit()




    #Loads data from a database into the application
    @property
    def load_state(self):
        pass



# amity = Amity()
# amity.create_room('narnia-Office')
# #amity.load_people()
# amity.print_unallocated()
# amity.print_allocations()
