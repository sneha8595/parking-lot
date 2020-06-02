from common.logrequest import log_request

class Vehicle:
    def __init__(self, reg_no, color, parking_spot=None, ticket=None):
        self.__reg_no = reg_no
        self.__color = color.upper()
        self.__parking_spot = parking_spot
        self.__ticket = ticket

    def __repr__(self):
        return "{}: {}".format(self.__reg_no, self.__color.upper())

    def assign_parking_spot(self, parking_spot, ticket):
        self.__parking_spot = parking_spot
        self.__ticket = ticket
        log_request("{} Vehicle entered: {} | Ticket: {}".format(self, self.__parking_spot, ticket))

    def deassign_parking_spot(self):
        self.__parking_spot = None
        log_request("{} Vehicle exited | Ticket: {}".format(self, self.get_ticket()))

    def get_color(self):
        return self.__color

    def get_ticket(self):
        return self.__ticket

    def get_reg_no(self):
        return self.__reg_no
