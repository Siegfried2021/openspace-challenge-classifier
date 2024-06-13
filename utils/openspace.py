import Table from table.py
import random


class Openspace:
    def __init__(self, n):        
        self.number_of_tables = n
        self.tables = [Table() for _ in range(n)]
        
    def organize(self, names):
        random.shuffle(names)
        for name in names :
            for table in self.tables:
                while table.has_free_spot():
                    table.assign_seat(name)
    
    def display():
        
                
                    
                
                
                     
                 
                        
    
  


    


