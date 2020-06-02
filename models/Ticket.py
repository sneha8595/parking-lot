import uuid
from enum import Enum


class TicketStatus(Enum):
  ACTIVE,PAID,LOST = 1, 2, 3

class Ticket:
    def __init__(self,vehicle_reg_no,parking_slot, status=TicketStatus.ACTIVE):
        self.__ticket_id = str(uuid.uuid1())
        self.__status = status
        self.__vehicle_reg_no=vehicle_reg_no
        self.__parking_slot=parking_slot

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.__ticket_id, self.__status, self.__vehicle_reg_no,self.__parking_slot)

    def save_to_db(self):
        # save ticket to db, which logs all the entries and exits
        pass

    def modify_status(self, status):
        self.__status = status
        self.save_to_db()

    def get_status(self):
        return self.__status

