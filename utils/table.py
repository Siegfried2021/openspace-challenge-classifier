





























class Table:
    def __init__(self, capacity : int):
        self.capacity = capacity 
        self.seats:[Seat(i + 1) for i in range(capacity)] # type: ignore

    def __str__(self) -> str:
        return f"{self.capacity} {self.seats}"
    
    def has_free_spot():
        return bool #True if a spot is available 

    def assign_seat(name):
        #that places someone at the table
        return 

    def left_capacity():
        return  #that returns an integer