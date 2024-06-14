# Create a class called Seat
class Seat:
    def __init__(self, free: bool = True, occupant: str = ""):
        """
        A class representing a seat in the openspace.
        There are two attributes: 
            free which is a boolean : Indicates if the seat is free.
            occupant which is a string : The name of the person occupying
        """
        self.free = free
        self.occupant = occupant
        
    # function set_occupant(name) which allows the program to assign someone a seat if it's free
    def set_occupant(self, name: str):

        """
        Assigns a person to the seat if it's free.
        Args:
            name (str): The name of the person to occupy the seat.
        Returns:
            bool: True if the occupant was set successfully, False otherwise.
        """

        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False 
    
     # function remove_occupant() which remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):
        """
        Removes the person from the seat.
        Returns:
            str: The name of the person who was occupying the seat.
        """
        if not self.free:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        return ""

    def __str__(self) -> str:
        return f"Seat(free={self.free}, occupant='{self.occupant}')"

class Table:
    """
    A class representing a table in the openspace.
    Attributes:
        capacity (int): The capacity of the table.
        seats : A list of seats at the table.
    """
    def __init__(self, capacity : int = 4):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]
    
    # function that returns a boolean (True) if a spot is available at the table
    def has_free_spot(self) -> bool:
        """
        Checks if there is a free seat at the table.
        Returns:
            bool: True if there is a free seat, False otherwise.
        """
        return any(seat.free for seat in self.seats) #True if a spot is available 

    # function that places someone at the table
    def assign_seat(self, name: str):
        """
        Assigns a person to a free seat at the table.
        Args:
            name (str): The name of the person to assign to a seat.
        Returns:
            bool: True if the person was assigned a seat, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return False 

    # function that returns an integer referring to the number of free spots left at the table
    def left_capacity(self) -> int:
        """
        Returns the number of free seats at the table.
        Returns:
            int: The number of free seats.
        """
        return  sum(1 for seat in self.seats if seat.free)
    
    def __str__(self) -> str:
        return f"Table(capacity={self.capacity}, seats=[{', '.join(str(seat) for seat in self.seats)}])"