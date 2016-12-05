class Amity(object):
    name = 'Amity'
    def __init__(self):
        pass

    #a method to handle room creation. it requires a room name as the input
    @property
    def create_room(self):
        pass

    #a method to implement adding a person to a room.
    @property
    def add_person(self):
        pass

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
