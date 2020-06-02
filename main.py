from models.ParkingLot import ParkingLot

if __name__ == '__main__':
    max_vehicles=int(input("Total number of vehicles:\n"))
    parking_lot = ParkingLot(max_vehicles)

    #enters a vehicle
    parking_lot.allot_slot_to_vehicle('10','red')
    parking_lot.allot_slot_to_vehicle('11', 'black')
    parking_lot.allot_slot_to_vehicle('12', 'black')

    color="red"
    parking_lot.get_vehicles_based_on_color(color)
    parking_lot.get_parking_slot_of_vehicle('10')
    parking_lot.get_slots_based_on_color(color)
    parking_lot.get_available_slots()

    #exits
    parking_lot.deallot_slot_to_vehicle('10')






