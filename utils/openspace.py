from utils.table import Table
import random
import pandas as pd


class Openspace:
    """
        A class representing the openspace with multiple tables.
        Attributes:
        tables ([Table]): A list of tables in the openspace.
        number_of_tables (int): The number of tables in the openspace.
    """
    def __init__(self, n: int=6):        
        self.number_of_tables = n
        self.tables = [Table() for _ in range(n)]
        
    def organize(self, names):
        """
        Randomly assign people to seats in the tables.
        Args:
            names ([str]): A list of names to assign to seats.
        """
        random.shuffle(names)
        for name in names :
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
       
    def display(self):
        """
        Display the tables and their occupants.
        """
        for i, table in enumerate(self.tables):
            table_name = f"table{i+1}:"
            occupants = []
            for seat in table.seats:
                occupants.append(seat.occupant)
            string_ocupants = ", ".join(occupants)
            print(f"{table_name} has {len(occupants)} occupants: {string_ocupants}")
    
        result = 0
        for table in self.tables:
            result += table.left_capacity()
        print(f"The openspace has {result} free seats!")

    def store(self, filename: str):
        """
        Store the seating arrangement in an excel file.
        Args:
            filename (str): The path to the excel file.
        """
        lines = []
        for i, table in enumerate(self.tables):
            table_name = f"table{i+1}:"
            for seat in table.seats:
                if seat.free == False:
                    occupant_name = seat.occupant
                    lines.append([table_name, occupant_name])
                    
        file = pd.DataFrame(lines, columns=["Table name", "Occupants"])
        file.to_excel(filename, index=False)
