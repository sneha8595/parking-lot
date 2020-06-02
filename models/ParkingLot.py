import uuid

from models.ParkingSpot import ParkingSpot
from models.Ticket import Ticket, TicketStatus
from models.Vehicle import Vehicle
from common.logrequest import log_request


class ParkingLot:
    def __init__(self, max_vehicles):
        self.MAX_VEHICLES = max_vehicles
        self.__parking_spots = {}
        for _ in range(self.MAX_VEHICLES):
            slot_id = str(uuid.uuid1())
            self.__parking_spots[slot_id] = ParkingSpot(slot_id)

    def allot_slot_to_vehicle(self, vehicle_no, color):
        vehicle = Vehicle(vehicle_no, color)
        if self.is_full():
            log_request("Parking full!")
            return
        slot = self.get_first_available_slot()
        ticket = Ticket(vehicle_no,slot)
        slot.assign_vehicle(vehicle, ticket)
        vehicle.assign_parking_spot(slot, ticket)
        # log_request("Available slots count after entering: " + str(len(self.get_available_slots())))
        return ticket

    def deallot_slot_to_vehicle(self, vehicle_no):
        slot = self.get_parking_slot_of_vehicle(vehicle_no)
        if not slot:
            log_request("vehicle not found")
            return
        slot.get_ticket().modify_status(TicketStatus.PAID)
        slot.get_vehicle().deassign_parking_spot()
        slot.remove_vehicle()
        # log_request("Available slots count after exiting: " + str(len(self.get_available_slots())))
        return slot

    def get_vehicles_based_on_color(self, color):
        vehicles = [value.get_vehicle() for key, value in self.__parking_spots.items() if
                    not value.is_free() and value.get_vehicle().get_color() == color.upper()]
        log_request("Vehicles of color {} are: {}".format(color.upper(), vehicles))
        return vehicles

    def get_available_slots(self):
        available_slots = [value for key, value in self.__parking_spots.items() if
                           value.is_free()]
        log_request("Available slots are: {}".format(available_slots))

    def get_first_available_slot(self, ):
        for key in self.__parking_spots:
            if self.__parking_spots.get(key).is_free():
                return self.__parking_spots[key]
        return None

    def is_full(self):
        for key in self.__parking_spots:
            if self.__parking_spots.get(key).is_free():
                return False
        return True

    def get_parking_slot_of_vehicle(self, vehicle_reg_no):
        slot = None
        for key, value in self.__parking_spots.items():
            if not value.is_free() and value.get_vehicle().get_reg_no() == vehicle_reg_no:
                slot = value
                break
        log_request("Parking slot is: " + str(slot))
        return slot

    def get_slots_based_on_color(self, color):
        slots = [value for key, value in self.__parking_spots.items() if
                 not value.is_free() and value.get_vehicle().get_color() == color.upper()]
        log_request("Slots of color {} are: {}".format(color.upper(), slots))
        return slots
