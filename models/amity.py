from models.room import Room, LivingSpace, Office

class Amity(object):
    name = 'Amity'
    def __init__(self):
        self.rooms = []

    """ a method to handle room creation. it requires a room name as the input """
    def create_room(self, name, type):
        try:
            if name.lower() not in [room.room_name.lower() for room in self.rooms]:
                """ check to see the type of room a person wishes to create """
                if type == 'L':
                    #create room of type LivingSpace if the type is L to denote livingSpace
                    room = LivingSpace(name)
                    self.rooms.append(room)
                else:
                    room = Office(name)
                    self.rooms.append(room)
            return room
        except NameError:
            return 'Sorry a room with the same name already exixts!'

    #a method to implement adding a person to a room.
    def add_person(self, first_name, second_name, accomodation=None):
        self.first_name = first_name
        self.second_name = second_name

    #a method to implement the reallocations of persons in Amity
    @property
    def reallocate_person(self):
        pass

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

    #retrives a room given the room name as input
    @property
    def print_room(self):
        pass

    #Persists all the data stored in the app to a SQLite database
    @property
    def save_state(self):
        pass

    #Loads data from a database into the application
    @property
    def load_state(self):
        pass
