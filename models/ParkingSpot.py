class ParkingSpot:
    def __init__(self, slot_id):
        self.__slot_id = slot_id
        self.__free = True
        self.__vehicle = None
        self.__ticket = None

    def __repr__(self):
        return self.__slot_id

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle, ticket):
        self.__vehicle = vehicle
        self.__ticket = ticket
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True

    def get_vehicle(self):
        return self.__vehicle

    def get_ticket(self): return self.__ticket
