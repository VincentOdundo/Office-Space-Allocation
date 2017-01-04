

class Room(object):
    """
    Base class that the class LivingSpace and Office inherit from
    """
    """ constructor to the room class to instantiate a room with a name"""
    def __init__(self, room_name):
        self.room_name = room_name
        self.people = []


class LivingSpace(Room):
    """
    Class LivingSpace is to expose a room of type LivingSpace and the number of occupants
    """
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.room_name = room_name
        self.no_of_occupants = 4
        self.current_occupancy = []
        self.room_type = 'LivingSpace'


class Office(Room):
    """
    Class Office is to expose a room of type Office and the number of occupants
    """
    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_name = room_name
        self.no_of_occupants = 6
        self.current_occupancy = []
        self.room_type = 'Office'
