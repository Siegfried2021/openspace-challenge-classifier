import Table from table.py
import random
import pandas as pd


class Openspace:
    def __init__(self, n: int):        
        self.number_of_tables = n
        self.tables = [Table(4) for _ in range(n)]
        
    def organize(self, names):
        random.shuffle(names)
        for name in names :
            for table in self.tables:
                while table.has_free_spot():
                    table.assign_seat(name)
    
    def display(self):
        for index, table in enumerate(self.tables):
            table_name = f"table{index(table)+1}"
        for table in self.tables:
            occupants = []
            for seat in table.seats:
                if seat.free == False:
                    occupants.append(seat.occupant)
        for table in self.tables:
            string_ocupants = ", ".join(occupants)
            print(f"{table_name} has {len(occupants)} occupants: {string_ocupants}")
    
    def store(self, filename):
        lines = []
        for index, table in enumerate(self.tables):
            table_name = f"table{index(table)+1}"
            for seat in table.seats:
                if seat.free == False:
                    occupant_name = seat.occupant
                    lines.append([table_name, occupant_name])
                    
        file = pd.DataFrame(lines, columns=["Table name", "Occupants"])
        file.to_excel("openspace_state.xlsx", index=False)