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
        
    # Creat function set_occupant(name) which allows the program to assign someone a seat if it's free
    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name
            self.free = False
        else: 
            print(f"Seat is already occupied by {self.occupant}")
           
     # Creat function remove_occupant() which remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):
        if self.free == False:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        else:
            print(f"The seat is free")