from models.room import Room, LivingSpace, Office
from models.person import Person, Fellow, Staff
from models.database import AmityRooms, Persons, create_db, Base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
import random

class Amity(object):
    name = 'Amity'
    def __init__(self):
        self.rooms = []
        self.people = []
        self.unallocated = []

    def create_room(self, office_type, room_name):
        """ a method to handle room creation. it requires a room name as the input """
        if room_name not in [room.room_name for room in self.rooms]:
            if office_type == 'Living':
                room = LivingSpace(room_name)
                self.rooms.append(room)
            else:
                room = Office(room_name)
                self.rooms.append(room)
        else:
            return '{} room exists or you cannot create a room with the same name twice!'.format(room_name)

    def add_person(self, first_name, second_name, person_type, accomodation=None):
        """ a method to implement adding a person to a room."""
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type
        self.accomodation = accomodation
        message = 'person added successfully! \n'
        if not self.rooms:
            message += 'No rooms in amity yet!'
        #if person is a Staff assign an Office
        if person_type == 'Staff':
            new_person = Staff(first_name, second_name)
            for room in self.rooms:
                if (room.room_type == 'Office' and
                room.no_of_occupants > len(room.current_occupancy)):
                    room.current_occupancy.append(new_person)
                    new_person.alloted_office = room.room_name
                    message += new_person.first_name+' allocated to '+room.room_name+'\n'
                    message += new_person.first_name + ' has been assigned '+ str(new_person.person_identifier)+ ' as the person id!'
                    break
            else:
                message += new_person.first_name+' has not been assigned an Office but his ID is:{}! \n'.format(str(new_person.person_identifier))
                self.unallocated.append(new_person)
            self.people.append(new_person)
        #if a Person is a Fellow and requires accomodation
        elif person_type == 'Fellow' and accomodation == 'Y':
            new_person = Fellow(first_name, second_name)
            #check for a vacant living room and assign a fellow
            for room in self.rooms:
                if (room.room_type == 'Living' and
                room.no_of_occupants > len(room.current_occupancy)):
                    room.current_occupancy.append(new_person)
                    new_person.alloted_living_space = room.room_name
                    message += new_person.first_name+' allocated to '+room.room_name
                    message += new_person.first_name + ' has been assigned '+ str(new_person.person_identifier)+ ' as the person id!'
                    break
            else:
                message += new_person.first_name+' has not been assigned a Living Space! \n'
            #check for a vacant office and allocate the fellow
            for room in self.rooms:
                if (room.room_type == 'Office' and
                room.no_of_occupants > len(room.current_occupancy)):
                    room.current_occupancy.append(new_person)
                    new_person.alloted_office = room.room_name
                    message += new_person.first_name+' allocated to '+room.room_name
                    message += new_person.first_name + ' has been assigned '+ str(new_person.person_identifier)+ ' as the person id!'
                    break
            else:
                message += new_person.first_name+' has not been assigned an Office but his ID is:{}! \n'.format(str(new_person.person_identifier))
                self.unallocated.append(new_person)
            self.people.append(new_person)
        else:
            new_person = Fellow(first_name, second_name)
            for room in self.rooms:
                if (room.room_type == 'Office' and
                room.no_of_occupants > len(room.current_occupancy)):
                    room.current_occupancy.append(new_person)
                    new_person.alloted_office = room.room_name
                    self.people.append(new_person)
                    message += new_person.first_name+' allocated to '+room.room_name
                    message += new_person.first_name + ' has been assigned '+ str(new_person.person_identifier)+ ' as the person id!'
                    break
            else:
                message += new_person.first_name+' has not been assigned an Office but his ID is:{}! \n'.format(str(new_person.person_identifier))
                self.unallocated.append(new_person)
        return message


    #a utility function to check a room exixts
    def check_room_exits(self, room_name):
        for room in self.rooms:
            if room.room_name.lower() == room_name.lower():
                return room
        return False

    def reallocate_person(self, identifier, room_name):
        """ a method to implement the reallocations of persons in Amity """
        found_person = None
        found_room = None
        for person in self.people:
            if person.person_identifier == int(identifier):
                found_person = person
                break
        else:
            return 'Person Not Found!'

        # Check if the room_name exist and is not full
        for room in self.rooms:
            if (room.room_name == room_name and
                    room.no_of_occupants > len(room.current_occupancy)):
                found_room = room
                break
        else:
            return "The room {} does not exist or is full".format(room_name)

        # if found_person is a staff and need accomodation return error message:
        message = 'assigning a staff to a livingSpace is not allowed!'
        if found_person.person_type == 'Staff' and found_room.room_type == "livingSpace":
            return message

        # remove person from previous room and reallocate them to the new room
        for previous_room in self.rooms:
            if found_person in previous_room.current_occupancy:
                previous_room.current_occupancy.remove(found_person)
        found_room.current_occupancy.append(found_person)
        return 'Reallocation was successfull'

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
        allocations = ''
        if not self.rooms:
            return 'No rooms created yet!'
        for room in self.rooms:
            allocations += room.room_name+"\n"
            if len(room.current_occupancy) > 0:
                for person in room.current_occupancy:
                    allocations += " ".join([person.first_name,person.second_name,'('+person.person_type+')\n'])
            else:
                allocations += "there are no people in the room\n"
        return allocations

    #Prints a list of unallocated people to the screen
    def print_unallocated(self, args):
        output = ""
        if self.unallocated:
            output += '*****************************************************************\n'
            output += 'LIST OF UNALLOCATED PERSONS\n'
            output += ", ".join([(person.first_name+' '+person.second_name+' '+'('+person.person_type+')\n')
            for person in self.unallocated])
        else:
            output += "there are no unallocated persons!"
        #output to a file
        if args:
            with open(args, 'wt') as filename:
                filename.write(output)
        else:
            return output

    #retrives a room with persons in the room given room name as input
    def print_room(self, room_name):
        retrieved_room = self.check_room_exits(room_name)
        if retrieved_room:
            print(retrieved_room.room_name)
            print('------------------------------------------------------------')
            print (", ".join([(person.first_name+' '+person.second_name+' '+'('+ person.person_type+ ')')
            for person in retrieved_room.current_occupancy]))
        else:
            return "No occupants in the room or room empty!"

    #Persists all the data stored in the app to a SQLite database
    def save_state(self, dbname='Amity'):
        engine = create_db(dbname)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        #retrieve offices from the Database to allow in comparisons and avoid redundancy
        rooms_from_db = select([AmityRooms])
        result = session.execute(rooms_from_db)
        room_names_from_db = [row.room_name for row in result]
        for room in self.rooms:
            if room.room_name not in room_names_from_db:
                new_room = AmityRooms(room_name=room.room_name, room_type=room.room_type)
                session.add(new_room)
                session.commit()

        #retrive persons from the Database to allow in comparison and avoid redundancy
        people_from_db = select([Persons])
        result = session.execute(people_from_db)
        people_from_db =[row.person_identifier for row in result]
        for person in self.people:
            if person.person_identifier not in people_from_db:
                alloted_living = ''
                if person.person_type == 'Staff':
                    alloted_living = None
                else:
                    alloted_living = person.alloted_living_space
                new_person = Persons(fname=person.first_name, lname=person.second_name,
                                    person_identifier=person.person_identifier,
                                    role=person.person_type,
                                    office_allocated=person.alloted_office, living_allocated=alloted_living)
                session.add(new_person)
                session.commit()

    #Loads data from a database into the application
    def load_state(self, dbname='Amity'):
        engine = create_db(dbname)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()

        rooms_from_db = select([AmityRooms])
        result = session.execute(rooms_from_db)
        for room in result:
            if room.room_type == 'Office':
                self.create_room('Office', room.room_name)
            else:
                self.create_room('Living', room.room_name)

        success_message = 'load state success!'
        persons_from_db = select([Persons])
        result = session.execute(persons_from_db)
        for person in result:
            if person.role == 'Staff':
                new_person = Staff(person.fname, person.lname)
                new_person.alloted_office = person.office_allocated
                new_person.person_identifier = person.person_identifier
                self.people.append(new_person)
                for room in self.rooms:
                    if new_person.alloted_office == room.room_name:
                        room.current_occupancy.append(new_person)
                        break
            else:
                new_person = Fellow(person.fname, person.lname)
                new_person.alloted_office = person.office_allocated
                new_person.alloted_living_space = person.living_allocated
                new_person.person_identifier = person.person_identifier
                self.people.append(new_person)
                for room in self.rooms:
                    if new_person.alloted_office == room.room_name:
                        room.current_occupancy.append(new_person)
                        break
                for room in self.rooms:
                    if new_person.alloted_living_space == room.room_name:
                        room.current_occupancy.append(new_person)
                        break
        print('load success!')
