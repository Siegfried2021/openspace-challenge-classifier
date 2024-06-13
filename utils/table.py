# Create a class called Seat
class Seat:
    def __init__(self, free: bool = True, occupant: str = ""):
        """
        There are two attributes: 
            free which is a boolean.
            occupant which is a string.
        """
        self.free = free
        self.occupant = occupant
        
    # function set_occupant(name) which allows the program to assign someone a seat if it's free
    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name
            self.free = False
        else: 
            print(f"Seat is already occupied by {self.occupant}")
           
     # function remove_occupant() which remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):
        if self.free == False:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        else:
            print(f"The seat is free")

class Table:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)] # type: ignore

    def __str__(self) -> str:
        return f"{self.capacity}: {self.seats}"
    
    # function that returns a boolean (True) if a spot is available at the table
    def has_free_spot(self):
        return any(seat.free for seat in self.seats) #True if a spot is available 

    # function that places someone at the table
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
            return 

    # function that returns an integer referring to the number of free spots left at the table
    def left_capacity(self):
        return  sum(1 for seat in self.seats if seat.free)