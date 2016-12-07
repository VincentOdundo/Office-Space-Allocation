"""
Base class that the class LivingSpace and Office inherit from
"""

class Room(object):
    """ constructor to the room class to instantiate a room with a name"""
    def __init__(self, room_name):
        self.room_name = room_name

"""
Class LivingSpace is to expose a room of type LivingSpace and the number of occupants
"""
class LivingSpace(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_name = room_name
        self.no_of_occupants = 4

"""
Class LivingSpace is to expose a room of type Office and the number of occupants
"""
class Office(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_name = room_name
        self.no_of_occupants = 6
